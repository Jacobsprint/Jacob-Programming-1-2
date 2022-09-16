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
  def plant1(self):
    self.m()
    self.m()
    self.m()
    self.m()
    self.put()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.tl()
  def plant4(self):
    self.plant1()
    self.plant1()
    self.plant1()
    self.plant1()
  
    
def main():
    """ Karel code goes here! """
    kt=ktools()
    kt.tl()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.tr()
    kt.plant4()
    
    
    
    
    
    

    
    
    
    
    
    
  
    pass


if __name__ == "__main__":
    run_karel_program()