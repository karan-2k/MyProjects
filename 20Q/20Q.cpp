#include <iostream>
#include <fstream>
#include <string>

using namespace std;
// struct to store question/answer and yes/no pointer in the same entity.
struct node
{
    string question;
    node* R_yes;
    node* L_no;
};
  
node* root = NULL;

node* loadFile(fstream &fptr, char lr, node* prev = NULL)
{
    string str;
    node* root = NULL;
    getline(fptr, str);
    
    // check if current node(i.e. root) is a leaf node, if it is then backtrack to previous node (loadFile() returns to previous state in stack).
    if (str != "-") 
    {
        // new() assigns memory needed for new node and automatically assigns the data members to NULL or "".
        root = new node();
        root->question = str;
        
        // checking if current node(i.e. root) is to be linked to prev's left(no) or right(yes).
        if (lr == 'L') 
        {
            prev->L_no = root;
        }

        if (lr == 'R')
        {
            prev->R_yes = root;
        }

        // passing previous node to loadfile to link with new node.
        loadFile(fptr, 'L', root); 
        loadFile(fptr, 'R', root);
    }

    return root;
}
 
node* loadDatabase(string fileName)
{
    fstream ques;
    node* start_node;

    ques.open(fileName);
    start_node = loadFile(ques, '-');
    ques.close();
    
    return start_node;
}

void saveFile(node* root, fstream& Fptr)
{
    if (root == NULL)
    {
        Fptr << "-" <<endl;
    }
    else
    {
        Fptr << root->question <<endl;
        saveFile(root->L_no, Fptr);
        saveFile(root->R_yes, Fptr);
    }
}

void saveDatabase(string fileName)
{
    fstream saveF;
    node* start_node;

    saveF.open(fileName, ios::out);
    saveFile(root, saveF);
    saveF.close();
}

void learningFn(node* root)
{
    string animal;
    string question;
    string root_ques;
    node* old_ques = new node();
    node* new_animal = new node();

    cout << "What are you thinking about? : ";
    cin >> animal;
    
    cout << "How do you tell a " + animal + " from a " + root->question + " ? :";
    getchar();
    getline(cin, question);
   
    // assigning the correct question to 3 nodes, new question(root), new animal(new_animal) and old question(old_ques).
    old_ques->question = root->question;
    root->question =  question;
    new_animal->question = animal;
    
    root->L_no  = old_ques;
    root->R_yes = new_animal;
    // saves the current changes to file.
    saveDatabase("Test.txt");
}

void navigateTree(node* root)
{
    char response = NULL;

    while (root !=  NULL)
    {
        if (root->L_no == NULL)
        {
            cout << "Is it a " + root->question + "? (y/n) : ";
        }
        else 
        {
            cout << root->question + "? (y/n) : ";
        }
        cin >> response;

        if (response == 'n' && root->L_no == NULL)
        {
            cout << "You win :(" << endl;
            learningFn(root);
            break;
        }
       
        else if (response == 'y' && root->R_yes == NULL)
        {
            cout << "I win! :)" <<endl;
            break;
        }
        
        else if (response == 'n')
        {
            root = root->L_no;
        }
        
        else if (response == 'y')
        {
            root = root->R_yes;
        }

        else
        {
            cout << "Invalid Response" << endl;
        }
    }
}

int main()
{
    char reloadGame = 'y';

    root = loadDatabase("Test.txt");
    
    while (reloadGame == 'y')
    {
        navigateTree(root);

        cout << "Would you like to play again? : ";
        cin >> reloadGame;
    }
}
