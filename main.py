import streamlit as st

lorem_ipsum = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis "
               "accumsan urna quis magna condimentum, sed faucibus velit auctor. "
               "Vestibulum sodales, turpis ac lobortis imperdiet, velit enim "
               "consequat libero, sed tincidunt eros elit eget elit. "
               "Pellentesque gravida mauris posuere pretium efficitur. "
               "Donec sit amet aliquet nunc. Nunc orci ex, pellentesque "
               "malesuada felis ut, venenatis facilisis velit. Aenean purus "
               "massa, pulvinar nec mi ut, laoreet bibendum nulla. Nulla "
               "sodales maximus elit, eu auctor mi fermentum sit amet. "
               "Mauris ac turpis ligula. Nam dictum mollis urna, vitae "
               "finibus diam. Mauris vitae quam vel dui aliquet feugiat in et "
               "eros. Donec non lobortis erat.")

st.header('Beautiful picture', divider='rainbow')
st.image("./assets/images/CarinaNebulaWebb.jpg")
st.write(lorem_ipsum)
