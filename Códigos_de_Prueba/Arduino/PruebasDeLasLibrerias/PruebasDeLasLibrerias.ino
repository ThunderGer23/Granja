#include <LCDWIKI_TOUCH.h>
#include <LCDWIKI_KBV.h>
#include <LCDWIKI_GUI.h>
#include <SoftwareSerial.h>

LCDWIKI_KBV lcd(ILI9488,40,38,39,43,41);
LCDWIKI_TOUCH touch(53,52,50,51,44); 

// Configuraciones iniciales
void setup() {
  Serial.begin(9600);
//  Serial.println(lcd.Get_Display_Width());  //Mide de 320 pixeles la LCD    496.47
//  Serial.println(lcd.Get_Display_Height()); //Mide de 480 pixeles la LCD    2,045.46
  lcd.Init_LCD();
  lcd.Set_Rotation(0);
  touch.TP_Init(lcd.Get_Rotation(),lcd.Get_Display_Width(),lcd.Get_Display_Height());
}

bool isPress(int x, int y){
    if(touch.x < lcd.Get_Display_Height()){
        
      }
  }
// Ya comenzamos a utilizar todas nuestras "Configuraciones iniciales" del _setup_
void loop() {
  touch.TP_Scan(0);
  Serial.println(touch.TP_Get_State());

  uint16_t px = 0;
  uint16_t py = 0;
  lcd.Draw_Rectangle(150,200,250,400);
  if(touch.TP_Get_State()>64 && TP_PRES_DOWN){
      py = touch.y;
      px = touch.x;
      Serial.println();
      Serial.print(px);
      Serial.print("\t");
      Serial.print(py);
      Serial.println();
      //for(int i = 0; i<=lcd.Get_Display_Width(); i++){}
  }
  
  
  delay(1000);
  
}
