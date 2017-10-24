#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <math.h>

int main(int argumentcount, char **arguments)
{
//particle names vector
std::vector<std::string> nametokens;
//X,Y vector vectors
std::vector<float> Xv;
std::vector<float> Yv;
//X,Y Position vectors
std::vector<float> X;
std::vector<float> Y;
//vector for time args
std::vector<std::string> cmdLineTime;
//individual input string for handling
std::string lineString;
//holders for apending vectors
std::string itemName;
float g,vol1,vol2,timex,pos1,pos2;
std::string::size_type sz;
std::string kk;
int args,timetot,i,parttotal,j,k,h;
//skips first argument which is program name
int argCount = 1;
int partnum=0;
int checkinit = 0;
//loop placing times entered at run in vectors

for(args=(argumentcount-1); args>=1; args--)
{//minus 1 argumentcount for programname accounting.
	lineString=arguments[argCount];
	if((std::isalpha(lineString[0])))
	{
		std::cout << "enterd \n";
		return 2;

	}
	else
	{
	cmdLineTime.push_back(arguments[argCount]);
	std::cout <<arguments[argCount] << '\n';
	argCount++;
	}
}
std::cout << "enter values \n";

//while loop for entering particles
while(getline (std::cin, lineString))
{//loop checking for input strings
//std::cout <<lineString << "\n";
std::stringstream D (lineString);


//count number of tolkens

int numspaces = 0;
//char nextChar;
int ischar = 0;
for (int i=0; i<int(lineString.length()); i++)
	{// checks each character in the string
		//nextChar = lineString.at(i); // gets a character
			if (isspace(lineString[i]))
			{//if space add to numofspaces
			numspaces++;
			}
			if((numspaces >= 1) && (std::isalpha(lineString[i])))
			{//after first space if a letter set is char to return 1
				ischar++;
			}
	}
numspaces+=1;//add 1 for total token count

if((numspaces<=4) || (numspaces>=6) || (ischar>0))
	{//checks if there are anything other than 5 total arguements or
	 // a letter in number spot
	return 1;
	}
else
	{
	for(int i=1; i<=5; i++)
		{//push each tolken into a vector cout for troubleshooting
			if (i==1)
				{
				D >> itemName;
				nametokens.push_back(itemName);
				//std::cout<<itemName<<"\n";
				}
			else if (i==2)
			{
				D >> g;
				X.push_back(g);
				//std::cout<<g<<"\n";
			}
			else if (i==3)
			{
				D >> g;
				Y.push_back(g);
				//std::cout<<g<<"\n";
			}
			else if (i==4)
			{
				D >> g;
				Xv.push_back(g);
				//std::cout<<g<<"\n";
			}
			else if (i==5)
			{
				D >> g;
				Yv.push_back(g);
				//std::cout<<g<<"\n";
			}
		}


	}//else ends
std::cout << "enter values \n";



}//while ends

int nocoll =0; //change to a 1 if collision detected and keep added for more than 1

while(!checkinit)
{//checking for initial postion overlap
	//xposition example
	//a h b; a h c; a h d
	//b h c; b h d;
	//c h d
	// h=sqrt(x**2 + y**2)
	//if no over lap checkinit = 1, if not return 1;
	parttotal = nametokens.size() -1;// total number of particles starting w/ 0
	for(i=0; i<=(parttotal);i++) //minus one for last comparison is skipped
	{//move to next vector to multiply
		j=i;
		for(j=j+1; j<parttotal;j++)//j=1 to skip  over current pos values
			{//calculated a H b , a H c, a H total
			pos1 = X[j] - X[j-1];
			pos2 = Y[j] - Y[j -1];
			pos1 = pos1 * pos1;
			pos2 = pos2 * pos2;
			pos1= pos1 + pos2;
			h=sqrt(pos1);
			std::cout<<h<<"\n";
			if(h<=10)
				{//if particles overlap return a 1
				nocoll=1;
				}
			}
	}
		checkinit = 1;
}





if(!nocoll)
{//if there are no collisions detected
	timetot= cmdLineTime.size() - 1;//number of times entered
	parttotal = nametokens.size() -1;
	for(i=0; i<=timetot; i++)
		{//loop over all entered times
			kk = cmdLineTime[i];
			timex= std::stof(kk, &sz);
				for(partnum=0; partnum<=parttotal; partnum++)
					{//loop over one particle
						//X cords movement by time
						pos1 = X[partnum];
						vol1= Xv[partnum];
						X[partnum] = pos1 + (vol1*timex);
						//Y cords movement by time
						pos1 = Y[partnum];
						vol1= Yv[partnum];
						Y[partnum] = pos1 + (vol1*timex);
						//particle moved
						std::cout<<"particle moved"<<"\n";
						std::cout<< nametokens[partnum]<<" "<<X[partnum]<<" "<<Y[partnum]<<" "<< Xv[partnum]<< " "<<Yv[partnum]<<"\n";

					}
		}
}


}//main ends



/* find time where there would be a collison,
 * fingure out collosion,
 * then move time forward.
 * for simple answer v1 = v2 ; v2 = v1
 */
