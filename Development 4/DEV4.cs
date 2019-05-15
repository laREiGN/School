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
		self.name = name;
		self.damage = damage;
		self.healthPoints = 100;
	}
	public TakeDamage(int damage){
		self.healthPoints = self.healthPoints - damage;
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
		self.make = make;
		self.model = model;
		self.speed = 0;
	}
	public SpeedUp(int x){
		self.speed = self.speed + x;
	}
	public SlowDown(int x){
		self.speed = self.speed - x;
	}
	public bool IsSpeeding(int limit){
		if (self.speed > limit){
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
		self.x = x;
		self.y = y;
	}
}

class Turtle{
	public Position position;
	public bool penOn;

	public Turtle(){
		self.penOn = false;
		self.position = new Position(0,0)
	}
	public Pen(bool x){
		self.penOn = x
	}
	public Right(int x){
		self.position.x = self.position.x + x
	}
	public Left(int x){
		self.position.x = self.position.x - x
	}
	public Up(int x){
		self.position.y = self.position.y - y
	}
	public Down(int x){
		self.position.y = self.position.y - y
	}
}

    ############################
    ####    Unit 0, BA9:    ####
    ############################

