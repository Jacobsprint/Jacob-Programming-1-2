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
  def bp(self) -> bool:
    """Beepers present"""
    return beepers_present()
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
  def beepersq(self):
    """Pick all beepers in square"""
    self.m()
    if self.bp():
      self.pick()
    else:  #Otherwise...
      self.ta()
      self.m()
      self.tr()

  def beepersqm(self, num):
    for nmber in range(num):
      self.beepersq()
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
  def setup(self):
    self.mm(2)
    self.tl()
    self.m()
    self.tr()
    
def main():
    """ Karel code goes here! """
    kt=ktools()
    kt.setup()
    kt.beepersqm(16)
    
    pass


if __name__ == "__main__":
    run_karel_program()