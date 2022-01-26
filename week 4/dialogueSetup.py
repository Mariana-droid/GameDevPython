from dialogue import Dialogue

#Lord forgive me for the names I'm about to give these objects
HelloJ = Dialogue("Joana")
HelloJ.set_speech("Hello my name is Joana")

ExitJ = Dialogue("Joana")
ExitJ.set_answer("Well, got to go")


Father = Dialogue("Joana")
Father.set_answer("Tell me about your father")
Father.set_speech("I have nothing to say about him.")

WhenFather = Dialogue("Joana")
WhenFather.set_answer("When was the last time you talked to him?")
WhenFather.set_speech("I don't recall")

HelloJ.add_option(Father)
HelloJ.add_option(ExitJ)
Father.add_option(WhenFather)
Father.add_option(ExitJ)
WhenFather.add_option(HelloJ)