// Copyright 2017 Keval Khara kevalk@bu.edu

#include <iostream>
#include <sstream>
#include <math.h>
#include <string>
#include <algorithm>
using namespace std;

class Vector 
{
public:
	double x, y;
	Vector(double q, double w) {		// constructor
		x = q;
		y = w;
	};
	Vector operator+(const Vector& other) const {
		return Vector(this->x + other.x, this->y + other.y);
	}
	Vector operator-(const Vector& other) const {
		return Vector(this->x - other.x, this->y - other.y);
	}
	Vector operator*(const double& c ) const {
		return Vector(this->x * c, this->y * c);
	}
	Vector operator/(const double& c) const {
		return Vector(this->x / c, this->y / c);
	}
	double normalize() {
		return sqrt(this->x * this->x + this->y *  this->y);
	}
	double dot(const Vector& b) {
		return (this->x*b.x + this->y*b.y);
	}
};

class particle        		// attributes of a particle
{
public:
	particle(){};
	string pID;
	double x_pos, y_pos, x_vel, y_vel;
	void pos_update(double dt);		// dt is the time elapsed between 2 time inputs
	void Collision(particle &other);
	double Distance(const particle &other);
	double timeToCollision(const particle &other);
	void print();
};

void particle:: pos_update(double dt) {
	x_pos = x_pos + x_vel * dt;
	y_pos = y_pos + y_vel * dt;
}

double particle::Distance(const particle &other) {
	double distance;
	distance = pow((this->x_pos - other.x_pos),2) + pow((this->y_pos - other.y_pos),2);
	return distance;
};
// calculating the time to collision
double particle::timeToCollision(const particle &other) {
	double A = this->x_pos - other.x_pos;
	double B = this->x_vel - other.x_vel;
	double C = this->y_pos - other.y_pos;
	double D = this->y_vel - other.y_vel;
	double E = 2.0 * A*B*C*D - A*A*D*D - B*B*C*C +  100.0 * (B*B + D*D);
	double F = A*B + C*D;
	double G = sqrt(E);
	double timeToCollision = 0.0;
	if  (E > 0 && (-F - G) >= 0)
		timeToCollision = (-F - G) / (B*B + D*D);
	else 
		timeToCollision = -1.0; 
	return timeToCollision;
}

// dictionary for each pair and their collision time
struct col2parts {
	int pair[2];
	double collisionTime;
};
// for multiple particles
class multpart
{
public:
	multpart();
	double time_inputs[1000];
	double current_time;
	double final_time;
	particle particles[1000];
	int particle_count;
	int ti_count;
	void update(double dt);		// update positions
	double nextCollisionTime;	// next collision time
	particle col_parts[2];
	col2parts nextcol_time(double current_time);
	void print(double current_time);
	void multpart_exec();
};

multpart::multpart() {}

void multpart::update(double dt) {
	for (int i = 0;i < this->particle_count;i++) 
		this->particles[i].pos_update(dt);
}

col2parts multpart::nextcol_time(double cur_time) {
	int i, j, pairnumber = 0;
	pairnumber = particle_count * (particle_count-1)/2;		//n(n-1)/2
	double nocol_time = 1e20;			// when no collision will occur
	double temp = 0.0;
	col2parts col_array[pairnumber];
	col2parts parties;
	int pair_count = 0;
	for (i = 0; i < particle_count-1; i++) {
		for (j = i + 1; j < particle_count; j++) {
			temp = particles[i].timeToCollision(particles[j]);
			col_array[pair_count].collisionTime = temp;
			col_array[pair_count].pair[0] = i;
			col_array[pair_count].pair[1] = j;
			if (temp != -1 && temp <= nocol_time) 
				nocol_time = temp;
			pair_count++;
		}
	}
	if (nocol_time == 1e20) {
		parties.pair[0] = 0;
		parties.pair[1] = 0;
		parties.collisionTime = 1e20;
	}
	else {
		for (i = 0; i < pair_count; i++) {
			if (col_array[i].collisionTime == nocol_time) {
				parties.pair[0] = col_array[i].pair[0];
				parties.pair[1] = col_array[i].pair[1];
				parties.collisionTime = nocol_time + cur_time;
			}
			else 
				continue;
		}
	}
	return parties;
};

void multpart::print(double current_time) {
	cout << current_time << endl;
	for (int i = 0;i < particle_count;i++) 
		particles[i].print();	
};

void multpart::multpart_exec() {
	int m, n, count = 0;
	col2parts cp;
	while (current_time <= final_time) {
		cp = nextcol_time(current_time);
		nextCollisionTime = cp.collisionTime;
		m = cp.pair[0];
		n = cp.pair[1];
		while (time_inputs[count]< nextCollisionTime && count < ti_count) {
			update(time_inputs[count] - current_time);
			current_time = time_inputs[count];
			print(current_time);
			count++;
		}
		update(nextCollisionTime - current_time);
		particles[m].Collision(particles[n]);
		current_time = nextCollisionTime;
	}
}

int main(int argcount, char **argv)
{
	multpart multi;
	double time = 0.0;
	double temp;
	
	// get time inputs list
	int time_count = 0;
	string str_tmp;
	for (int i = 0; i < argcount-1; i++)
	{	
		str_tmp = argv[i+1];
		for (int j = 0; argv[i+1][j] != '\0'; j++){
			if(argv[i+1][j] != '.' && (argv[i+1][j] >'9' || argv[i+1][j] < '0'))
				return 2;
		}
		time = stod(argv[i+1]);
		if (time < 0)
			return 2;
		else
		{
			multi.time_inputs[time_count] = time;
			time_count++;
		}
	}
	if (time_count == 0)
		return 2;
	for (int i = 0; i < time_count-1; i++) {		// sorting time inputs
		for (int j = i+1; j < time_count; j++) {
			if (multi.time_inputs[i] > multi.time_inputs[j]) {
				temp = multi.time_inputs[i];
				multi.time_inputs[i] = multi.time_inputs[j];
				multi.time_inputs[j] = temp;
			}
		}
	}
	multi.ti_count = time_count;
	multi.final_time = multi.time_inputs[time_count - 1];
	
	// get input positions and velocities
	int line_count = 0;
	string ID, str;
	double x, y, vx, vy;
	char error=' ';
	while (getline(cin,str)) {
		if(stringstream(str) >> ID >> x >> y >> vx >> vy){
			multi.particles[line_count] = particle();
			multi.particles[line_count].pID = ID;
			multi.particles[line_count].x_pos = x;
			multi.particles[line_count].y_pos = y;
			multi.particles[line_count].x_vel = vx;
			multi.particles[line_count].y_vel = vy;
		}
		else	
			return 1;		// invalid input
		
		stringstream(str) >> ID >> x >> y >> vx >> vy >> error;
		if (error != ' ')
			return 1;			
		line_count++;		// extra input values
	};
	multi.particle_count = line_count;
	multi.multpart_exec();	//begin
    return 0;

