
import emitcallback

def test_basic() -> None:
	
	s = emitcallback.Signal[[]]()

	s.connect(lambda: print("Helllo World!"))
	s.emit()
