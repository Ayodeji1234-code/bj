import streamlit as st
from pathlib import Path
import time

# -------------------------------------------------------
# CUSTOM STYLING
# -------------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#fff8f8;
}

h1{
    color:#d63384;
    text-align:center;
}

h3{
    text-align:center;
}

.message{
    background:transparent;
    padding:25px;
    border-radius:15px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# OPENING ANIMATION
# -------------------------------------------------------

placeholder = st.empty()

placeholder.markdown("# 🎁 Preparing Your Surprise...")

progress = st.progress(0)

for i in range(101):
    progress.progress(i)
    time.sleep(0.03)

placeholder.empty()
progress.empty()

# -------------------------------------------------------
# BALLOONS
# -------------------------------------------------------

st.balloons()

# -------------------------------------------------------
# TITLE
# -------------------------------------------------------

st.title("From Me To You ❤️")

st.write("")

# -------------------------------------------------------
# MESSAGE
# -------------------------------------------------------

message = """
Baby🌚,

Before you watch this video…

I want you to pause for just a moment and know how grateful I am that God wrote our love story.

Out of everyone in this world, He chose you for me.

And somehow…

He chose me for you.

I don’t think words will ever fully express what you mean to me, but today, I’ll try.

You are my answered prayer.

My peace.

My safe place.

My best friend.

My greatest blessing.

Thank you for choosing me.

Thank you for loving me through every smile, every tear, every distance, every misunderstanding, and every beautiful memory we’ve created together.

Thank you for believing in us.

Thank you for never giving up on me.

Thank you for becoming my home.
❤️
"""

st.markdown(
    f'<div class="message">{message}</div>',
    unsafe_allow_html=True
)

st.write("")
st.write("")

# -------------------------------------------------------
# BUTTON TO REVEAL VIDEO
# -------------------------------------------------------

from pathlib import Path

if st.button("🎥 Click Here For Your Video"):

    video_path = Path(__file__).parent / "VID-20260705-WA0056.mp4"

    if video_path.exists():

        st.success("Enjoy your surprise! ❤️")

        with open(video_path, "rb") as video_file:
            st.video(video_file.read())

    else:
        st.error(f"Video not found: {video_path}")

# -------------------------------------------------------
# FINAL MESSAGE
# -------------------------------------------------------

st.write("")
st.write("")

st.markdown(
"""
### 🌹

There are thousands of people we’ll meet throughout our lives.

But there is only one person I want to spend forever growing with.

That’s you.

Years from now…

When our hair turns grey…

When our children ask how we met…

When life becomes busy…

When days become difficult…

I pray we never forget this feeling.

I pray we always remember that love is a choice.

And every single day…

I will continue choosing you.

Again.

Again.

And again.

One Last Promise…

If one day life becomes difficult…

Come back here.

Watch this again.

Read these words again.

And remember…

There is someone praying for you every day.

Someone cheering for you.

Someone who believes in you.

Someone who loves you more than words could ever explain.

That someone…

is me.

Forever.

❤️

#FOREVERSTARTSWITHTHEO’s
🎂🎉❤️
"""
)

st.write("")

