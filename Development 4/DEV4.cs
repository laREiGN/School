#Unit 0, BA1:

public Student(string firstName, string lastName, int studentNumber, string[] courses)
	{
	this.firstName = firstName;
	this.lastName = lastName;
	this.studentNumber = studentNumber;
	this.courses = courses;
	}

#Unit 0, BA2:

public string MakeSound()
	{
	string soundMade = this.name + " says " + this.sound;
	return soundMade;
	}

public void Feed()
	{
	this.weight = this.weight + 0.5;
	}

#Unit 0, BA3:

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

#Unit 0, BA4:

class Planet
	{
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

#Unit 0, BA5:

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