import tkinter as tk
from tkinter import messagebox



evidence = []

game_over = False


suspects = {
    "Maya": {
        "role": "Hotel Receptionist",
        "description": "Works at the hotel reception desk.",
        "statements": {
            "alibi": (
                "I was working at the reception desk all night. "
                "I never left my post."
            ),
            "alex": (
                "Alex came down to the lobby around 9:30 PM. "
                "He looked worried."
            ),
            "night": (
                "I heard a loud sound around 11:30 PM, "
                "but I couldn't tell where it came from."
            )
        }
    },

    "Arjun": {
        "role": "Alex's Friend",
        "description": "Alex's close friend who came to the hotel.",
        "statements": {
            "alibi": (
                "I came to the hotel to meet Alex. "
                "I left around 10:00 PM."
            ),
            "alex": (
                "Alex had been acting strangely that evening. "
                "He said someone was following him."
            ),
            "watch": (
                "Alex never went anywhere without his watch. "
                "He was wearing it when I saw him."
            )
        }
    },

    "Daniel": {
        "role": "Hotel Manager",
        "description": "The manager has access to every room.",
        "statements": {
            "alibi": (
                "I was checking the security cameras "
                "in the office around midnight."
            ),
            "room": (
                "Nobody entered Room 204 through the main hallway."
            ),
            "key": (
                "Only hotel management and housekeeping "
                "have access to emergency keys."
            )
        }
    },

    "Sara": {
        "role": "Hotel Guest",
        "description": "A guest staying on the same floor.",
        "statements": {
            "alibi": (
                "I was in my room all evening. "
                "I didn't leave."
            ),
            "window": (
                "I heard something near the window around midnight. "
                "It sounded like someone moving outside."
            ),
            "alex": (
                "I didn't know Alex personally. "
                "I only saw him once in the hallway."
            )
        }
    }
}


# =========================================================
# CLUES
# =========================================================

clues = {
    "room": "⌚ A broken watch was found under the bed.",

    "door": "🚪 The door has no signs of forced entry.",

    "window": (
        "🪟 The window was open, but there are "
        "no footprints outside."
    ),

    "desk": "🔑 A small hotel key was found inside the desk."
}




root = tk.Tk()

root.title("The Last Room")

root.geometry("760x900")

root.resizable(False, False)



def add_evidence(clue):

    if clue not in evidence:

        evidence.append(clue)

        status_label.config(
            text="🔎 New evidence discovered!"
        )

        update_evidence()

    else:

        status_label.config(
            text="You've already discovered this clue."
        )


def examine_room():

    add_evidence(
        clues["room"]
    )


def inspect_door():

    add_evidence(
        clues["door"]
    )


def check_window():

    add_evidence(
        clues["window"]
    )


def search_desk():

    add_evidence(
        clues["desk"]
    )


def update_evidence():

    evidence_text.config(
        state="normal"
    )

    evidence_text.delete(
        "1.0",
        tk.END
    )

    if not evidence:

        evidence_text.insert(
            tk.END,
            "No evidence discovered yet."
        )

    else:

        for index, clue in enumerate(
            evidence,
            start=1
        ):

            evidence_text.insert(
                tk.END,
                f"{index}. {clue}\n\n"
            )

    evidence_text.config(
        state="disabled"
    )



def question_suspect(name):

    interrogation = tk.Toplevel(root)

    interrogation.title(
        f"Interrogation - {name}"
    )

    interrogation.geometry(
        "600x550"
    )

    interrogation.resizable(
        False,
        False
    )


    tk.Label(
        interrogation,
        text=f"🗣️ INTERROGATING {name.upper()}",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(
        interrogation,
        text=suspects[name]["role"],
        font=("Arial", 13, "italic")
    ).pack()



    dialogue = tk.Text(
        interrogation,
        width=65,
        height=13,
        font=("Arial", 11),
        wrap="word"
    )

    dialogue.pack(
        padx=20,
        pady=15
    )

    dialogue.config(
        state="disabled"
    )


    def show_message(message):

        dialogue.config(
            state="normal"
        )

        dialogue.delete(
            "1.0",
            tk.END
        )

        dialogue.insert(
            tk.END,
            message
        )

        dialogue.config(
            state="disabled"
        )


    question_frame = tk.Frame(
        interrogation
    )

    question_frame.pack(
        pady=10
    )

    # Alibi
    tk.Button(
        question_frame,
        text="Where were you?",
        width=20,
        command=lambda: show_message(
            f"{name}: "
            f"{suspects[name]['statements']['alibi']}"
        )
    ).grid(
        row=0,
        column=0,
        padx=5,
        pady=5
    )

    # Alex
    tk.Button(
        question_frame,
        text="Ask about Alex",
        width=20,
        command=lambda: show_message(
            f"{name}: "
            f"{suspects[name]['statements']['alex']}"
        )
    ).grid(
        row=0,
        column=1,
        padx=5,
        pady=5
    )

    if name == "Maya":

        tk.Button(
            question_frame,
            text="Ask about the key",
            width=20,
            command=lambda: show_message(
                maya_key_question()
            )
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        tk.Button(
            question_frame,
            text="Ask about the noise",
            width=20,
            command=lambda: show_message(
                f"Maya: "
                f"{suspects['Maya']['statements']['night']}"
            )
        ).grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

    elif name == "Arjun":

        tk.Button(
            question_frame,
            text="Ask about the watch",
            width=20,
            command=lambda: show_message(
                arjun_watch_question()
            )
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

    elif name == "Daniel":

        tk.Button(
            question_frame,
            text="Ask about the room",
            width=20,
            command=lambda: show_message(
                f"Daniel: "
                f"{suspects['Daniel']['statements']['room']}"
            )
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        tk.Button(
            question_frame,
            text="Ask about the key",
            width=20,
            command=lambda: show_message(
                f"Daniel: "
                f"{suspects['Daniel']['statements']['key']}"
            )
        ).grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

    elif name == "Sara":

        tk.Button(
            question_frame,
            text="Ask about the window",
            width=20,
            command=lambda: show_message(
                f"Sara: "
                f"{suspects['Sara']['statements']['window']}"
            )
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )



    tk.Button(
        interrogation,
        text="🚪 Leave Interrogation",
        width=25,
        height=2,
        command=interrogation.destroy
    ).pack(
        pady=20
    )




def maya_key_question():

    if clues["desk"] in evidence:

        return (
            "Maya: That key...\n\n"
            "Maya: I didn't know it was missing.\n\n"
            "Maya: Only the manager normally keeps "
            "those emergency keys."
        )

    return (
        "Maya: I don't know anything about "
        "a missing hotel key."
    )


def arjun_watch_question():

    if clues["room"] in evidence:

        return (
            "Arjun: Alex's watch was broken?\n\n"
            "Arjun: That's strange.\n\n"
            "Arjun: He was wearing it when I saw "
            "him earlier that evening."
        )

    return (
        "Arjun: Alex always wore his watch. "
        "He never took it off."
    )


def accuse_suspect():

    if len(evidence) < 3:

        messagebox.showwarning(
            "Not Enough Evidence",
            "You need at least 3 pieces of evidence "
            "before making an accusation."
        )

        return

    accusation_window = tk.Toplevel(root)

    accusation_window.title(
        "Make Your Accusation"
    )

    accusation_window.geometry(
        "450x400"
    )

    accusation_window.resizable(
        False,
        False
    )

    tk.Label(
        accusation_window,
        text="⚖️ FINAL ACCUSATION",
        font=("Arial", 22, "bold")
    ).pack(pady=25)

    tk.Label(
        accusation_window,
        text=(
            "Who do you believe is responsible\n"
            "for Alex's disappearance?"
        ),
        font=("Arial", 13),
        justify="center"
    ).pack(pady=10)

    selected_suspect = tk.StringVar()

    for name in suspects:

        tk.Radiobutton(
            accusation_window,
            text=name,
            variable=selected_suspect,
            value=name,
            font=("Arial", 12)
        ).pack(
            pady=5
        )

    def submit_accusation():

        choice = selected_suspect.get()

        if not choice:

            messagebox.showwarning(
                "Choose a suspect",
                "Select a suspect first."
            )

            return

        accusation_window.destroy()

        show_ending(choice)

    tk.Button(
        accusation_window,
        text="🔎 Submit Accusation",
        width=25,
        height=2,
        command=submit_accusation
    ).pack(
        pady=20
    )




def show_ending(choice):

    global game_over

    game_over = True

    ending_window = tk.Toplevel(root)

    ending_window.title(
        "Case Result"
    )

    ending_window.geometry(
        "600x500"
    )

    ending_window.resizable(
        False,
        False
    )

    tk.Label(
        ending_window,
        text="📁 CASE RESULT",
        font=("Arial", 24, "bold")
    ).pack(pady=25)

    if choice == "Daniel":

        result = (
            "🏆 CASE SOLVED!\n\n"
            "Daniel was responsible for Alex's disappearance.\n\n"
            "The hotel key found in the desk was an emergency "
            "key accessible to management. The locked-room "
            "evidence and Daniel's statements revealed "
            "contradictions in his story.\n\n"
            "You solved the mystery!"
        )

    else:

        result = (
            "❌ WRONG ACCUSATION\n\n"
            f"You accused {choice}.\n\n"
            "The evidence does not support this accusation.\n\n"
            "The real answer was Daniel, the hotel manager.\n\n"
            "Review the evidence and try again."
        )

    tk.Label(
        ending_window,
        text=result,
        font=("Arial", 12),
        justify="center",
        wraplength=520
    ).pack(
        padx=30,
        pady=20
    )

    tk.Button(
        ending_window,
        text="🔄 Close Case",
        width=20,
        height=2,
        command=ending_window.destroy
    ).pack(
        pady=20
    )



def new_game():

    evidence.clear()

    status_label.config(
        text="New investigation started."
    )

    update_evidence()



tk.Label(
    root,
    text="🔎 THE LAST ROOM",
    font=("Arial", 28, "bold")
).pack(
    pady=20
)


tk.Label(
    root,
    text="📁 CASE #001",
    font=("Arial", 18, "bold")
).pack()


tk.Label(
    root,
    text=(
        "Alex Morgan has disappeared from Room 204.\n"
        "The door was locked from the inside.\n"
        "Four people were present in the hotel."
    ),
    font=("Arial", 13),
    justify="center"
).pack(
    pady=12
)



tk.Label(
    root,
    text="👥 SUSPECTS",
    font=("Arial", 18, "bold")
).pack(
    pady=8
)


suspect_frame = tk.Frame(root)

suspect_frame.pack()


suspect_buttons = [
    ("👩 Maya\nReceptionist", "Maya", 0, 0),
    ("👨 Arjun\nAlex's Friend", "Arjun", 0, 1),
    ("👨 Daniel\nHotel Manager", "Daniel", 1, 0),
    ("👩 Sara\nHotel Guest", "Sara", 1, 1)
]


for text, name, row, column in suspect_buttons:

    tk.Button(
        suspect_frame,
        text=text,
        width=20,
        height=3,
        command=lambda person=name:
            question_suspect(person)
    ).grid(
        row=row,
        column=column,
        padx=8,
        pady=5
    )


tk.Label(
    root,
    text="🔎 INVESTIGATION",
    font=("Arial", 18, "bold")
).pack(
    pady=12
)


investigation_frame = tk.Frame(root)

investigation_frame.pack()


tk.Button(
    investigation_frame,
    text="🔍 Examine Room",
    width=20,
    height=2,
    command=examine_room
).grid(
    row=0,
    column=0,
    padx=8,
    pady=4
)


tk.Button(
    investigation_frame,
    text="🚪 Inspect Door",
    width=20,
    height=2,
    command=inspect_door
).grid(
    row=0,
    column=1,
    padx=8,
    pady=4
)


tk.Button(
    investigation_frame,
    text="🪟 Check Window",
    width=20,
    height=2,
    command=check_window
).grid(
    row=1,
    column=0,
    padx=8,
    pady=4
)


tk.Button(
    investigation_frame,
    text="🗄️ Search Desk",
    width=20,
    height=2,
    command=search_desk
).grid(
    row=1,
    column=1,
    padx=8,
    pady=4
)



status_label = tk.Label(
    root,
    text="What will you investigate?",
    font=("Arial", 12, "italic")
)

status_label.pack(
    pady=12
)

tk.Label(
    root,
    text="📋 EVIDENCE COLLECTED",
    font=("Arial", 18, "bold")
).pack(
    pady=8
)


evidence_text = tk.Text(
    root,
    width=75,
    height=7,
    font=("Arial", 10),
    wrap="word"
)

evidence_text.pack()


action_frame = tk.Frame(root)

action_frame.pack(
    pady=18
)


tk.Button(
    action_frame,
    text="⚖️ Make Accusation",
    width=22,
    height=2,
    font=("Arial", 11, "bold"),
    command=accuse_suspect
).grid(
    row=0,
    column=0,
    padx=10
)


tk.Button(
    action_frame,
    text="🔄 New Game",
    width=22,
    height=2,
    command=new_game
).grid(
    row=0,
    column=1,
    padx=10
)



update_evidence()

root.mainloop()