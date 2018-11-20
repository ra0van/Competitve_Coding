using System;
using System.Collections.Generic;
using System.Linq;

namespace MindSum
{
    public class Node
    {
        public long key;
        public int level;
        public Node left, right;

        public Node(long item, int i)
        {
            key = item;
            left = right = null;
            level = i;
        }
    }

    public class BinaryTree
    {
        public Node root;

        public BinaryTree(long key)
        {
            root = new Node(key, 0);
        }

        public long sum(long l)
        {
            long s = 0;
            while (l != 0)
            {
                s += (l % 10);
                l = l / 10;
            }

            return s;
        }

        public void increaseTree(Node n, long d)
        {
            List<Node> li = new List<Node>();
            li.Add(n);
            for (int i = 0; i < 12; i++)
            {
                List<Node> list1 = new List<Node>(li);

                foreach (Node node in list1)
                {
                    Node n1 = new Node(node.key + d, node.level + 1), n2 = new Node(sum(node.key), node.level + 1);
                    node.left = n1;
                    node.right = n2;
                    li.Remove(node);
                    li.Add(n1); li.Add(n2);
                }
            }
        }

        public Tuple<long, long> min(Node node)
        {
            if (node.left == null && node.right == null)
            {
                return new Tuple<long, long>( node.key, node.level);
            }
            else
            {

                Tuple<long, long> leftMin = min(node.left), rightMin = min(node.right);
                long leftValue = leftMin.Item1, rightValue = rightMin.Item1;
                long leftHeight = leftMin.Item2, rightHeight = rightMin.Item2;
                Tuple<long, long> result = null;


                if (leftValue == rightValue)
                {
                    if (node.key <= leftValue)
                    {
                        result = new Tuple<long, long>(node.key, node.level);
                    }
                    else
                    {
                        if (leftHeight < rightHeight)
                        {
                            result = leftMin;
                        }
                        else
                        {
                            result = rightMin;
                        }
                    }
                }
                else if (leftValue < rightValue)
                {
                    result = (leftValue < node.key) ? leftMin : new Tuple<long, long>(node.key, node.level);
                }
                else
                {
                    result = (rightValue < node.key) ? rightMin : new Tuple<long, long>(node.key, node.level);
                }

                return result;
            }

        }
    }


    public class Program
    {

        public static void Main(string[] args)
        {
            int t = Convert.ToInt32(Console.ReadLine());

            for(int ti = 0; ti < t; ti++)
            {
                List<string> arr = Console.ReadLine().Split(' ').ToList();
                long n = Convert.ToInt64(arr[0]), d = Convert.ToInt64(arr[1]);
                BinaryTree tree = new BinaryTree(n);
                tree.increaseTree(tree.root, d);
                Tuple<long, long> result = tree.min(tree.root);
                Console.WriteLine(result.Item1.ToString() + " " +  result.Item2.ToString());
            }
        }
    }
}





