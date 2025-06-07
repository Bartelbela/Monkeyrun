# 🐵 Monkey Jump Spiel - Entwicklungsplan

## 📋 Übersicht
Ein 2D-Plattformspiel mit einem Affen als Hauptcharakter, der durch verschiedene Hindernisse navigiert und dabei Programmierkonzepte vermittelt.

---

## 🔧 Phase 1: Grundsetup (Tag 1-2)

### 1.1 Entwicklungsumgebung einrichten
- [ ] Python und pygame installieren (`pip install pygame`)
- [ ] Projektordner erstellen mit Unterordnern:
  ```
  monkey_game/
  ├── main.py
  ├── assets/
  │   ├── images/
  │   ├── sounds/
  │   └── fonts/
  ├── src/
  │   ├── __init__.py
  │   ├── game.py
  │   ├── player.py
  │   ├── obstacles.py
  │   └── ui.py
  └── README.md
  ```

### 1.2 Basis-Spielfenster erstellen
```python
# main.py - Grundgerüst
import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Monkey Jump - Programmieren lernen!")
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((135, 206, 235))  # Himmelblau
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()
```

---

## 🐒 Phase 2: Spieler-Charakter (Tag 3-4)

### 2.1 Monkey-Klasse erstellen
- [ ] **Programmierkonzept: Klassen & Objekte**
```python
# src/player.py
class Monkey:
    def __init__(self, x, y):
        self.x = x  # Variable
        self.y = y  # Variable
        self.width = 50
        self.height = 50
        self.vel_y = 0  # Geschwindigkeit
        self.on_ground = False
```

### 2.2 Bewegungssteuerung implementieren
- [ ] **Programmierkonzept: Eingabe-Verarbeitung & Bedingungen**
- [ ] Laufen (Links/Rechts)
- [ ] Springen
- [ ] Ducken
- [ ] Schwimmen (für Wasser-Level)

### 2.3 Monkey-Grafik
- [ ] Einfache Rechteck-Darstellung für Prototyp
- [ ] Später: Sprite-Animation für verschiedene Bewegungen

---

## 🚧 Phase 3: Hindernisse & Kollision (Tag 5-7)

### 3.1 Hindernisse erstellen
- [ ] **Programmierkonzept: Listen & Objekt-Verwaltung**
```python
# src/obstacles.py
class Obstacle:
    def __init__(self, x, y, obstacle_type):
        self.x = x
        self.y = y
        self.type = obstacle_type  # "rock", "palm", "water", "abyss"
```

### 3.2 Kollisionserkennung
- [ ] **Programmierkonzept: Algorithmen & Logik**
```python
def check_collision(monkey, obstacle):
    # Rechteck-Kollision
    if (monkey.x < obstacle.x + obstacle.width and
        monkey.x + monkey.width > obstacle.x and
        monkey.y < obstacle.y + obstacle.height and
        monkey.y + monkey.height > obstacle.y):
        return True
    return False
```

### 3.3 Verschiedene Hindernistypen
- [ ] **Kaktus**: Muss übersprungen werden
- [ ] **Palmen**: Muss übersprungen werden  
- [ ] **Wurzeln**: Muss geduckt werden
- [ ] **Wasser/Teich**: Muss geschwommen werden
- [ ] **Abgrund**: Muss mit präzisem Sprung überwunden werden

---

## 🎮 Phase 4: Spielmechanik (Tag 8-10)

### 4.1 Punktesystem
- [ ] **Programmierkonzept: Variablen & Zähler**
```python
class Game:
    def __init__(self):
        self.score = 0  # Aktueller Punktestand
        self.time_survived = 0
        
    def update_score(self):
        self.score += 1  # Pro überstandene Sekunde
```

### 4.2 Geschwindigkeitssteigerung
- [ ] **Programmierkonzept: Schleifen & Zeitberechnung**
```python
def increase_difficulty(self):
    # Je länger gespielt, desto schneller
    if self.time_survived % 30 == 0:  # Alle 30 Sekunden
        self.game_speed += 0.5
```

### 4.3 Game Loop
- [ ] **Programmierkonzept: Endlosschleifen & Zustandsverwaltung**
- [ ] Kontinuierliche Bewegung
- [ ] Hindernisse spawnen
- [ ] Kollisionsprüfung
- [ ] Score-Update

---

## 🎨 Phase 5: Grafiken & Animationen (Tag 11-13)

### 5.1 Sprite-System
- [ ] **Programmierkonzept: Dateien & Resourcen-Management**
```python
class SpriteManager:
    def __init__(self):
        self.monkey_sprites = {
            'run': [],  # Liste von Lauf-Bildern
            'jump': [],
            'duck': [],
            'swim': []
        }
    
    def load_sprites(self):
        # Bilder aus Dateien laden
        pass
```

### 5.2 Hintergrund-System
- [ ] Scrolling-Hintergrund
- [ ] Zufällige Hintergrundelemente
- [ ] Verschiedene Hintergründe je nach Schwierigkeit

### 5.3 Partikel-Effekte (Optional)
- [ ] Staub beim Laufen
- [ ] Spritzer beim Schwimmen

---

## 🔊 Phase 6: Audio (Tag 14-15)

### 6.1 Sound-System
- [ ] **Programmierkonzept: Dateien & Audio-Verarbeitung**
```python
class AudioManager:
    def __init__(self):
        self.sounds = {}
        self.background_music = None
    
    def load_sounds(self):
        self.sounds['jump'] = pygame.mixer.Sound('assets/sounds/jump.wav')
        self.sounds['collision'] = pygame.mixer.Sound('assets/sounds/hit.wav')
```

### 6.2 Sound-Effekte
- [ ] Sprung-Sound
- [ ] Kollisions-Sound
- [ ] Hintergrundmusik (Loop)

---

## 📊 Phase 7: UI & Menüs (Tag 16-18)

### 7.1 Benutzeroberfläche
- [ ] **Programmierkonzept: Text-Rendering & UI-Design**
```python
class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
    
    def draw_score(self, score):
        text = self.font.render(f"Punkte: {score}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))
```

### 7.2 Startmenü
- [ ] Titel-Screen
- [ ] "Spiel starten" Button
- [ ] "Beenden" Button

### 7.3 Game-Over Screen
- [ ] Endpunktzahl anzeigen
- [ ] Highscore-System
- [ ] "Neu starten" Option

---

## 🏆 Phase 8: Polishing & Features (Tag 19-21)

### 8.1 Programmier-Lernaspekte integrieren
- [ ] **Code-Kommentare als Storytelling**
- [ ] **Mini-Tutorials zwischen Leveln**
```python
# Storytelling-Beispiel:
# "Der Affe verwendet eine VARIABLE namens 'speed' um zu wissen, wie schnell er laufen soll!"
# "Mit einer IF-BEDINGUNG prüft er: 'Ist da ein Hindernis? Dann springe!'"
```

### 8.2 Schwierigkeitsgrade
- [ ] **Anfänger**: Langsame Geschwindigkeit, wenige Hindernisse
- [ ] **Fortgeschritten**: Mittlere Geschwindigkeit, mehr Variationen
- [ ] **Experte**: Schnell, komplexe Hinderniskombinationen

### 8.3 Achievements/Erfolge
- [ ] "Erste 100 Punkte" - **Konzept: Variablen**
- [ ] "10 Sprünge hintereinander" - **Konzept: Zähler & Schleifen**
- [ ] "5 Minuten überlebt" - **Konzept: Zeit-Messung**

---

## 🧪 Phase 9: Testing & Debugging (Tag 22-23)

### 9.1 Fehlerbehandlung
- [ ] **Programmierkonzept: Exception Handling**
```python
try:
    # Spiel-Code
    pass
except Exception as e:
    print(f"Fehler aufgetreten: {e}")
    # Graceful shutdown
```

### 9.2 Performance-Optimierung
- [ ] FPS-Monitoring
- [ ] Memory-Management für Sprites
- [ ] Effiziente Kollisionserkennung

---

## 📦 Phase 10: Deployment (Tag 24-25)

### 10.1 Packaging
- [ ] Requirements.txt erstellen
- [ ] Executable mit PyInstaller erstellen
- [ ] Asset-Dateien einbinden

### 10.2 Dokumentation
- [ ] README.md vervollständigen
- [ ] Spielanleitung schreiben
- [ ] Code-Kommentare überprüfen

---

## 🎯 Vermittelte Programmierkonzepte

| Konzept | Wo im Spiel | Schwierigkeit |
|---------|-------------|---------------|
| **Variablen** | Spieler-Position, Score, Geschwindigkeit | Anfänger |
| **Bedingungen (if/else)** | Kollisionserkennung, Sprung-Logik | Anfänger |
| **Schleifen** | Game Loop, Hindernis-Spawning | Anfänger |
| **Klassen & Objekte** | Monkey, Obstacle, Game-Klassen | Mittelstufe |
| **Listen** | Hindernisse verwalten, Sprites | Mittelstufe |
| **Funktionen** | Kollisionserkennung, Score-Update | Anfänger |
| **Event-Handling** | Tastatur-Eingaben | Mittelstufe |
| **Dateien** | Sprite/Sound-Loading | Fortgeschritten |

---

## ⏰ Zeitplan-Übersicht

- **Woche 1 (Tag 1-7)**: Setup + Grundmechanik
- **Woche 2 (Tag 8-14)**: Gameplay + Grafiken  
- **Woche 3 (Tag 15-21)**: Audio + UI + Polish
- **Woche 4 (Tag 22-28)**: Testing + Deployment + Buffer

---

## 💡 Zusätzliche Ideen für später

- [ ] **Level-Editor**: Spieler können eigene Hindernisparcours erstellen
- [ ] **Multiplayer**: Zwei Affen gleichzeitig
- [ ] **Story-Modus**: Verschiedene Umgebungen (Dschungel, Strand, Berge)
- [ ] **Code-Challenges**: Mini-Programmieraufgaben zwischen Leveln
- [ ] **Visual Scripting**: Simple drag-&-drop Programmierung für Kinder

---

## 🔗 Hilfreiche Ressourcen

- [Pygame Dokumentation](https://www.pygame.org/docs/)
- [Sprite-Ressourcen](https://opengameart.org/)
- [Sound-Effekte](https://freesound.org/)
- [Python Tutorials](https://docs.python.org/3/tutorial/)

---

*Viel Erfolg bei der Entwicklung! 🚀*