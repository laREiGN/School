    ############################
    ####    Unit 0, BA1:    ####
    ############################

public Student(string firstName, string lastName, int studentNumber, string[] courses)
	{
	this.firstName = firstName;
	this.lastName = lastName;
	this.studentNumber = studentNumber;
	this.courses = courses;
	}

    ############################
    ####    Unit 0, BA2:    ####
    ############################

public string MakeSound()
	{
	string soundMade = this.name + " says " + this.sound;
	return soundMade;
	}

public void Feed()
	{
	this.weight = this.weight + 0.5;
	}

    ############################
    ####    Unit 0, BA3:    ####
    ############################

class Rectangle
	{
	public double length;
	public double width;

	public Rectangle(double length, double width)
		{
		this.length = length;
		this.width = width;
		}

	public double Area()
		{
		double area = this.length * this.width;
		return area;
		}
	}

    ############################
    ####    Unit 0, BA4:    ####
    ############################

class Planet{
	public string name;
	public double distance;
	public double gravity;

	public Planet(string name, double distance, double gravity)
		{
		this.name = name;
		this.distance = distance;
		this.gravity = gravity;
		}

	public string Info()
		{
		string info = "Planet " + this.name + ", distance: " + this.distance + "AU, gravity: " + this.gravity;
		return info;
		}
	}

    ############################
    ####    Unit 0, BA5:    ####
    ############################

class Vector2
	{
	public double x;
	public double y;

	public Vector2(double x, double y)
		{
		this.x = x;
		this.y = y;
		}

	public Vector2 Times(double value)
		{
		return new Vector2(this.x * value, this.y * value);
		}

	public Vector2 Plus(Vector2 vectorused)
		{
		return new Vector2(this.x + vectorused.x, this.y + vectorused.y);
		}
	}

    ############################
    ####    Unit 0, BA6:    ####
    ############################

class Player{
	public string name;
	public int healthPoints;
	public int damage;

	public Player(string name, int damage){
		this.name = name;
		this.damage = damage;
		this.healthPoints = 100;
	}
	public TakeDamage(int damage){
		this.healthPoints = this.healthPoints - damage;
	}
}

    ############################
    ####    Unit 0, BA7:    ####
    ############################

class Car{
	public string make;
	public string model;
	public int speed;

	public Car(string make, string model){
		this.make = make;
		this.model = model;
		this.speed = 0;
	}
	public void SpeedUp(int x){
		this.speed = this.speed + x;
	}
	public void SlowDown(int x){
		this.speed = this.speed - x;
	}
	public bool IsSpeeding(int limit){
		if (this.speed > limit){
			return true;
		}
		else {
			return false;
		}

	}
}

    ############################
    ####    Unit 0, BA8:    ####
    ############################

class Position{
	public int x;
	public int y;
	
	public Position(int x, int y){
		this.x = x;
		this.y = y;
	}
}

class Turtle{
	public Position position;
	public bool penOn;

	public Turtle(){
		this.penOn = false;
		this.position = new Position(0,0);
	}
	public void Pen(bool x){
		this.penOn = x;
	}
	public void Right(int x){
		this.position.x = this.position.x + x;
	}
	public void Left(int x){
		this.position.x = this.position.x - x;
	}
	public void Up(int x){
		this.position.y = this.position.y + x;
	}
	public void Down(int x){
		this.position.y = this.position.y - x;
	}
}

    ############################
    ####    Unit 0, BA9:    ####
    ############################

class Point{
	public double x;
	public double y;

	public Point(double x, double y){
		this.x = x;
		this.y = y;
	}
}

class Line{
	public Point[,] points = new Point(2,2);

	public Lines(Point x, Point y){
		this.points[0, 0] = x.x;
		this.points[0, 1] = x.y;
		this.points[1, 0] = y.x;
		this.points[1, 1] = y.y;
	}
	public double Distance(){
		x1 = this.points[1, 0] - this.points[0, 0];
		y1 = this.points[1, 1] - this.points[0, 1];
		x1squared = x1 * x1;
		y1squared = y1 * y1;
		squared = x1squared + y1squared;
		distance = Math.Sqrt(squared);
		return distance;
	}

}

class Canvas{
	public Line[] lines; 
	public int numLines;

	public Canvas(int linesamt){
		this.lines = new Line[linesamt];
		this.numLines = 0;
	}
	public AddLine(Line line){
		this.lines[this.numLines] = line;
		this.numLines = this.numLines + 1;
	}
	public Undo(){
		if(this.numLines > 0){
			this.numLines = this.numLines - 1;
			this.lines[this.numLines] = null;
		}
		else{}
	}

}

