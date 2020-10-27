public class Solution{

      public int MaxInteger(int N){
            StringBuilder newNumber = new StringBuilder("");


            if (N > 0)
            {
                string number = N.ToString();
                bool stop = false;
                foreach (var t in number)
                {
                    if (5 >= (int)Char.GetNumericValue(t) && stop == false)
                    {
                        newNumber.Append("5");
                        newNumber.Append(t);
                        stop = true;

                    }
                    else
                    {

                        newNumber.Append(t);

                    }
                }
                if (stop == false)
                {
                    newNumber.Append("5");
                }
            }
            else if(N < 0)
            {
                string number = N.ToString();
                bool stop = false;
                foreach (var t in number)
                {
                    if (5 <= (int)Char.GetNumericValue(t) && stop == false)
                    {
                        newNumber.Append("5");
                        newNumber.Append(t);
                        stop = true;

                    }
                    else
                    {

                        newNumber.Append(t);

                    }
                }
                if (stop == false)
                {
                    newNumber.Append("5");
                }
            }else{
               newNumber.Append("50");    
            }
      
            return int.Parse(newNumber.ToString());
      
      }

}