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

void particle::print() {
	cout << pID << ' ' << x_pos << ' ' << y_pos << ' ' << x_vel << ' ' << y_vel << endl;
}
// implementing the collision formula using vectors
void particle::Collision(particle &other) {
	Vector p1 = Vector(this->x_pos, this->y_pos);
	Vector p2 = Vector(other.x_pos, other.y_pos);
	Vector v1 = Vector(this->x_vel, this->y_vel);
	Vector v2 = Vector(other.x_vel, other.y_vel);
	Vector axis1 = (p2 - p1);
	Vector axis2 = (p1 - p2);
	Vector v1axis = axis1 * (v1.dot(axis1)) / this->Distance(other);
	Vector v2axis = axis2 * (v2.dot(axis2)) / this->Distance(other);
	this->x_vel = (v2axis + v1 - v1axis).x;
	this->y_vel = (v2axis + v1 - v1axis).y;
	other.x_vel = (v1axis + v2 - v2axis).x;
	other.y_vel = (v1axis + v2 - v2axis).y;
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
