from trace_types import read_types

class test():

  def test_reading_type_string():
    t = read_type()
    a_variable = "testing"
    type_string = t.read(a_variable)
    assert(type_string["testing"] == "str")

  def test_reading_type_initial_none():
    t = read_type()
    assert(t.types() == 0)
  
  def test_reading_type_not_none():
    t = read_type()
    a_variable = "testing"
    type_string = t.read(a_variable)
    assert(len(type_string) == 1)

  def test_reading_type_to_json():
    t = read_type()
    type_string = t.to_json()
    assert(type_string != "")
