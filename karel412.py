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
      self.ta()
    else:  #Otherwise...
      self.m()
      self.put()
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
  def mp(self):
    self.m()
    self.put() 
  def karel412(self):
    self.m()
    self.tl()
    self.mp()
    self.ta()
    self.m()
    self.tl()
    self.m()
    self.tl()
    self.m()
    self.putm(2)
    self.ta()
    self.mm(2)
    self.tl()
    self.m()
    self.tl()
    self.m()
    self.putm(3)
    self.ta()
    self.mm(3)
    self.tl()
    self.mm(6)
    
def main():
    """ Karel code goes here! """
    kt=ktools()
    kt.karel412()





  
    pass


if __name__ == "__main__":
    run_karel_program()