#include <bits/stdc++.h>	

using namespace std;

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};

class Solution {
    public:
  		Node* insert(Node* root, int data) {
            if(root == NULL) {
                return new Node(data);
            } else {
                Node* cur;
                if(data <= root->data) {
                    cur = insert(root->left, data);
                    root->left = cur;
                } else {
                    cur = insert(root->right, data);
                    root->right = cur;
               }

               return root;
           }
        }
    void levelOrder(Node * root) {
        // If root is NULL simply return
        if(root==nullptr) return;
        // Create an "queue" data structure
        // It will store the elements of tree in an queue
        queue<Node*> levelQueue;
        // Push the root
        levelQueue.push(root);
        // Iterate over the tree
        while (!levelQueue.empty()) {
            // If the tree's left is not empty,
            // push it into the queue
            // same for right side
            if(levelQueue.front()->left!=nullptr)
                levelQueue.push(levelQueue.front()->left);
            if(levelQueue.front()->right!=nullptr)
                levelQueue.push(levelQueue.front()->right);
                
            // Finally print the data of 1st element in queue
            cout<<levelQueue.front()->data<<" ";
            // Remove the element
            levelQueue.pop();
        }
    }
}; //End of Solution

int main() {
  
    Solution myTree;
    Node* root = NULL;
    
    int t;
    int data;

    std::cin >> t;

    while(t-- > 0) {
        std::cin >> data;
        root = myTree.insert(root, data);
    }
  
	myTree.levelOrder(root);
    return 0;
}
