int r = D6;
int y = D5;
int g = D4;

void setup() {
  pinMode(r, OUTPUT);
  pinMode(y, OUTPUT);
  pinMode(g, OUTPUT);
  
  // register the cloud function
  Particle.function("toggle", toggle);
}



void loop() {
}

int toggle(String command)
{
    if (command.equals("red"))
    {
        digitalWrite(r, HIGH);
        digitalWrite(y, LOW);
        digitalWrite(g, LOW);
        return 1;
    } else if (command.equals("yellow"))
    {
        digitalWrite(r, LOW);
        digitalWrite(y, HIGH);
        digitalWrite(g, LOW);
        return 1;
    } else if (command.equals("green"))
    {
        digitalWrite(r, LOW);
        digitalWrite(y, LOW);
        digitalWrite(g, HIGH);
        return 1;
    } else {
        return -1;
    }
    
}


