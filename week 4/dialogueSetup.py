from dialogue import Dialogue

#Lord forgive me for the names I'm about to give these objects
HelloJ = Dialogue("Joana")
HelloJ.set_speech("Please ask me any questions you might have.")

ExitJ = Dialogue("Joana")
ExitJ.set_answer("Well, thanks for your time Ma'am.")

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

FirstTimeTalkingJ = Dialogue("Joana")
FirstTimeTalkingJ.set_speech("Hello, I'm Joana Grinstead. I'm the one who called you about my father.")

AckJ = Dialogue("Joana")
AckJ.set_answer("Yes, of course Mrs. Grinstead. When was the last time you saw Mr. Grinstead?")
AckJ.set_speech("The last time I saw him was a week ago. He left to go run errands and never came back.")

WhereJ = Dialogue("Joana")
WhereJ.set_answer("Did he say anything about where he was going?")
WhereJ.set_speech("No, he's usually really secretive about his errands. I'm not sure what he does at all, to be honest.")

IncredulousJ = Dialogue("Joana")
IncredulousJ.set_answer("Why did you only report him missing now?")
IncredulousJ.set_speech("I understand why you might find it odd, but he sometimes goes away on errands for days. I didn't think anything of it\n\
until we heard nothing from him for that time.")

FinalJ = Dialogue("Joana")
FinalJ.set_answer("I'm going to take a look around the house. Please stay here in case I need to ask you more questions.")

FirstTimeTalkingJ.add_option(AckJ)
FirstTimeTalkingJ.add_option(ExitJ)

AckJ.add_option(WhereJ)
AckJ.add_option(IncredulousJ)

WhereJ.add_option(FinalJ)
WhereJ.add_option(ExitJ)

IncredulousJ.add_option(FinalJ)
IncredulousJ.add_option(ExitJ)

