// concatenate the two strings

var string1 = "dwjlfer";
var string2 = "aaadewemtr";

var string3 = new char[string1.length+string2.length];

for(int i=0; i < string3.length; i++)
{
      if(i < string1.length)
            {
                  string3[i] = string1[i];
            }
      else
            {
                  string3[i] = string2[Math.abs(string3.length - i - string2.length)]; 
            }
}
