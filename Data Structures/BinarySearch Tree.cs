// Binary Tree :
// Binary Search Tree : {Left Nodes} < {root} < {Right Nodes}   // in the left the  you may find right < left subs
// Balanced Binary Search Tree : 
public class BST 
{
      private class Node
      {
            private int value;
            private Node leftChild;
            private Node rightChild;

            public Node(int value)
            {
                  this.value = value;
            }
      }

      private Node root;

      public void Insert(int value)   // O(log n)
      {
            if(root == null)  // STEP 0
                  root = new Node(value);

            var current = root;

            while(true)
            {
                  if(value < root.value)   // Step 1
                  {
                        if(!root.leftChild)  // root.leftChild is Null
                        {
                              root.leftChild = new Node(value);  // Step 3 as a validation and Insertion
                              break;
                        }
                        current = root.leftChild;  // Step 2 
                  }

                  else(value > root.value)  // Step 1
                  {
                        if(!root.rightChild)
                        {
                              root.rightChild = new Node(value);
                              break;
                        }
                        current = root.rightChild;  // Step 2 
                  }
            }

      }

      public bool find(int value)   // O(log n)
                                                // Just Assertion that the Value exists  .Contains returns a bool
      {
            var current = root;
            while(current) // while current != null
            {
                  if(value < current.value)
                        current = root.leftChild;
                  else if(value > current.value)
                         current = root.rightChild;
                  else
                        return true;      // else here means  ( value == current.value  )
            }

            return false;  // will be called when           current is null and break the loop
 
      }

      private bool isLeaf(Node node)
      {
            return node.leftChild == null && node.rightChild == null;
      }

      public int min()
      {
            // just a wrapper
            return minimumValue(root);
      }


      // this is for "normal Binary Tree", not Balanced Binary Search Tree   (in BST, the min is always at the left bottom !)
      // Binary Search Tree, the left is smaller than the right , smaller than the root
      // but in in normal Binary Tree,  left is smaller than root, and smaller than right, but right not necessary                                                                                         smaller than the root
      private int minimumValue(Node node)
      {
            var leftVlaue = minimumValue(node.leftChild);   
            var rightValue = minimumValue(node.rightChild); 
            
              // step2, you need to catch the value, after traversing, by applying the base condition
                  if(isLeaf(node))  // Base Condition to break the recursion
                        return node.value;

            // step1, you need to think like traversing the Tree with recursion calls    O(N)
            return  Math.Min(Math.Min(leftVlaue,rightValue), root.value);         
      }


      private int minValueForBST(Node node)
      {
            // we are going to Traverse to the most left bottom 

            var current = node;
            var lastElement = 0;

            while(current != null)
            {
                  lastElement = current;
                  current = current.leftChild;   // this will reach a null at the end, so i need to have a ref for                                    it before it going to null   // O(log N)
            }

            return lastElement.value;   
      }

}