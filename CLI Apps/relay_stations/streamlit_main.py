from io import StringIO
import streamlit as st



uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    
    file_contents = uploaded_file.read().decode("utf-8")
    # st.write(file_contents)
    

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    string_data = stringio.read()
    # st.write(string_data)


    stations = []
    conns = []
    for line in file_contents.split("\n"):
        if line and line[0] != "#":
            station_info = line.split(", ")
            stations.append(Node(int(station_info[0]),
                                 station_info[1],
                                 int(station_info[2]),
                                 int(station_info[3])))
            conns.append(line.split("(")[1].split(", "))
            
   
