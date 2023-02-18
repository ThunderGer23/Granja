//Sensor de nivel tipo boya
//Salida a relé, para Led  de agua
const int led = 4; //mi salida a la led es al pin 13
const int nivel = 5; //mido el nivel de agua a la DI9

void setup()
{
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(nivel, INPUT);
}

void loop()
{
  
  float sens = analogRead(nivel);
  Serial.println(sens);
   if (digitalRead(nivel)) {
    Serial.println(" Nivel bajo de Agua. Rellenar el tanque");
    digitalWrite(led, HIGH);
   }
   else{
    Serial.println("Nivel de agua correcto, se puede regar");
    digitalWrite(led, LOW);
   }
   delay(500);
}
