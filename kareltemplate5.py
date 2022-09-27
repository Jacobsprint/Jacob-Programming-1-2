from stanfordkarel import *

class ktools:
  def m(self):
    """Shorthand for move"""
    move()
  def tl(self):
    """Turn Left"""
    turn_left()
  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl ()
  def ta(self):
    """Turn Around"""
    self.tl()
    self.tl()
  def pick(self):
    """Pick Beeper"""
    pick_beeper()
  def put(self):
    """Put Beeper"""
    put_beeper()
  def put2(self):
    """Put two beepers in row"""
    self.put()
    self.m()
    self.put()
  def put5(self):
    """Put five beepers in a row"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()
  def fic(self) -> bool:
    """Front is Clear"""
    return front_is_clear()
  def fib(self) -> bool:
    """Front is blocked"""
    return not self.fic()
  def ric(self) -> bool:
    """Right is Clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True # Immediately leaves the function
    self.tl()
    return False
  def rib(self) -> bool:
    """Right is blocked"""
    return not self.ric()  
  def mazemove(self):
    """Maze Move"""
    if self.fib():
      self.tl()
    else:  #Otherwise...
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr()
          self.m()
    pass

  def mm(self, num):
    """Move Multiples"""
    for number in range(num):
      self.m()
  def pickm(self, num):
    """Pick Multiple"""
    for i in range(num-1):
      self.pick()
      self.m()
    self.pick()
  def putm(self,num):
    """Put Multiple"""
    for _ in range(num-1):
      self.put()
      self.m()
    self.put()
    
  pass
  
  def SOB(self) -> bool:
    """Standing on beeper"""
    return beepers_present()
  def jump(self):
    """Jump for 510"""
    while self.fic():
      self.m()
    self.tl()
    while self.rib():
      self.m()
    self.tr()
    self.m()
    self.tr()
    while self.fic():
      self.m()
    self.tl()

  def find(self):
    """Find for 515"""
    while not facing_north():
      self.tl()
    self.m()
    if not self.SOB():
      self.tl()
      self.m()
      self.tl()
      self.m()
    for _ in range(2):
      if not self.SOB():
        self.m()
        self.tl()
        self.m()
    pass

    
def main():
    """ Karel code goes here! """
    kt=ktools()
    


  
    pass


if __name__ == "__main__":
    run_karel_program()