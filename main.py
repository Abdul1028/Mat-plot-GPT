import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def plot_line_plot():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Sine Wave')

    return fig


def plot_scatter_plot(num_points):
    x = np.random.randn(num_points)
    y = np.random.randn(num_points)

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Scatter Plot')

    return fig


def plot_bar_plot(num_categories):
    categories = [chr(ord('A') + i) for i in range(num_categories)]
    values = np.random.randint(0, 10, size=num_categories)

    fig, ax = plt.subplots()
    ax.bar(categories, values)
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    ax.set_title('Bar Plot')

    return fig


# Streamlit app
st.title('Matplotlib ChatBot')

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []

if "plot_type" not in st.session_state:
    st.session_state.plot_type = None

if "plot_fig" not in st.session_state:
    st.session_state.plot_fig = None


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.plot_type is None:
    prompt = st.chat_input("What type of plot do you want? (line/scatter/bar)")
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        response = "Great! Please provide the required parameters, "
        st.session_state.messages.append({"role": "assistant", "content": response})
        if prompt.lower() in ['line', 'scatter', 'bar']:

            st.session_state.messages.append({"role": "user", "content": prompt})

            if prompt.lower() == 'scatter':
                st.session_state.plot_type = "scatter"
                response += "\nNumber of points:"
                with st.chat_message("assistant"):
                    st.markdown("You choose "+st.session_state.plot_type + " " +response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            elif prompt.lower() == 'bar':
                st.session_state.plot_type = "bar"
                response += "\nNumber of categories:"
                with st.chat_message("assistant"):
                    st.markdown("You choose " + st.session_state.plot_type + " " + response)
                st.session_state.messages.append({"role": "assistant", "content": response})

        else:
            response = f"Invalid plot type: {prompt}. Please choose from line, scatter, or bar."
            with st.chat_message("assistant"):
                st.markdown(response)
else:
    # if st.session_state.plot_fig is None and st.session_state.plot_type is not None:
    if st.session_state.plot_type is not None and st.session_state.plot_type == 'scatter':
        num_points = st.chat_input("Number of points:")
        if num_points:
            try:
                num_points = int(num_points)
                if num_points > 0:
                    st.session_state.messages.append(
                        {"role": "assistant", "content": "Number of points selected is " + str(num_points)})
                    st.session_state.plot_fig = plot_scatter_plot(num_points)
                    st.session_state.messages.append({"role": "assistant", "content": "Plot generated!"})
                    st.session_state.plot_type = None
                else:
                    st.session_state.messages.append({"role": "user", "content": num_points})
                    st.session_state.messages.append(
                        {"role": "assistant", "content": "Invalid number of points. Please enter a positive integer."})
            except ValueError:
                st.session_state.messages.append({"role": "user", "content": num_points})
                st.session_state.messages.append(
                    {"role": "assistant", "content": "Invalid input. Please enter a valid number."})
    elif st.session_state.plot_type == 'bar':
        num_categories = st.chat_input("Number of categories:")
        if num_categories:
            try:
                num_categories = int(num_categories)
                if num_categories > 0:
                    st.session_state.messages.append({"role": "user", "content": num_categories})
                    st.session_state.messages.append({"role": "assistant", "content": "Plot generated!"})
                    st.session_state.plot_fig = plot_bar_plot(num_categories)
                    st.session_state.plot_type = None
                else:
                    st.session_state.messages.append({"role": "user", "content": num_categories})
                    st.session_state.messages.append({"role": "assistant",
                                                      "content": "Invalid number of categories. Please enter a positive integer."})
            except ValueError:
                st.session_state.messages.append({"role": "user", "content": num_categories})
                st.session_state.messages.append(
                    {"role": "assistant", "content": "Invalid input. Please enter a valid number."})



if st.session_state.plot_fig is not None:
    st.pyplot(st.session_state.plot_fig)
    st.session_state.plot_fig = None
