import streamlit as st
import pandas as pd
from PIL import Image

st.text("Resume Format Web")


code = """
<!DOCTYPE html>
<html lang="en">

   <head>
     <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href='https://cdn.jsdelivr.net/npm/boxicons@2.0.5/css/boxicons.min.css' rel='stylesheet'>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
     <title>Document</title>
     </head>
     <body>

    <div>

        <div>
            <h1>RESUME</h1>
            <p>Contact: <a href="abcd.com">chetansolanki6393@gmail.com</a> </p>
            <p>LinkedIn: <a href="linkedin.com">https://www.linkedin .com/in/chetan-solanki-66a6842b5           </p>
            <p>GitHub: <a href='https://github.com/ChetaN7895'>github.com/ChetaN7895</a> </p>

        </div>

        <table>
            <tr>
                <td>
     

                    <img src="C:\\Users\\Education\\Downloads\\new.jpg" alt="chetanPic">
                </td>
                <td>
                    I am a passionate software engineer with expertise in problem-solving and algorithmic thinking. I love to explore various technologies and frameworks to develop efficient and scalable solutions. With a strong foundation in data structures and algorithms,
                    I strive to create robust and optimized code. I am constantly expanding my skills and staying up-to-date with the latest advancements in the field of software development.
                </td>
            </tr>
        </table>

        <section>
            <h2>Education</h2>

            <ul>
                <li>Bachelor of Technology in Computer Science, CLG Institute of Technology
                </li>
                <li>Govt Senior Secondary School SUMERPUR
                </li>
            </ul>

        </section>

        <section>
            <h2>Work Experience</h2>

            <div>
                <h3>
                    Software Engineer, Microsoft
                </h3>

                <p>  </p>
                <ul>
                    <li>
                        Developed and maintained web applications using HTML, CSS, and JavaScript, PYTHON

                    </li>
                    <li>Collaborated with cross-functional teams to design and implement software solutions
                    </li>
                    <li>Optimized code performance and improved application efficiency
                    </li>
                </ul>
            </div>

            <div>
                <h3>
                    WEB Development Engineer
                </h3>
                <p>
                
                </p>
                <ul>
                    <li>
                        Assisted in developing and testing modules
                    </li>
                    <li>Worked on bug and performance enhancement tasks
                    </li>
                </ul>
            </div>




        </section>

        <section>
            <h2>
                Skills
            </h2>

            <ul>
                <li>Java</li>
                <li>Marketing</li>
                <li>Python</li>
                <li>HTML</li>
                <li>CSS</li>
                <li>JS</li>
                <li>Editing</li>
            </ul>

        </section>

        <section>
            <h2>Achievements</h2>

            <ul>
                <li>Service Selection (Recommendation letter for Web Development Internship)
                </li>

            </ul>

        </section>

        <section>
            <h2>Projects</h2>

            <ul>
                <li>
                    <h3>Library Management System</h3>
                    <p>Library Management Application – developed a desktop application by using java swing and MYSQL server.
                    </p>
                    <p>Hosted Link: <a href="abcd.com">example.com/ecommerce</a> </p>
                    <p>GitHub Link: <a href="https://github.com/ChetaN7895">github.com</a> </p>
                </li>
                <li>
                    <h3>
                        Friendly Chat AppFriendly
                    </h3>
                    <p>Friendly Chat – An Android application making use of firebase, to help people connect and chat by sending messages and images, also having login options.
                    </p>
                    <p>Hosted Link: <a href="abcd.com"> example.com/blog</a> </p>
                    <p>GitHub Link: <a href="https://github.com/ChetaN7895">github.com/ChetanSolanki/blog</a> </p>
                </li>
                <li>
                    <h3>
                        Secure Messenger AppSecure
                    </h3>
                    <p>
                        Secure Messenger App – An Android application to have secure communication between the sender and recipient, using a number of cryptography algorithms like AES, DES, RSA techniques for encryption and decryption.
                    </p>
                    <p>Hosted Link: <a href="abcd.com"> example.com/dashboard</a> </p>
                    <p>GitHub Link: <a href="abcd.com">github.com/CHETAN/dashboard</a> </p>
                </li>
            </ul>

        </section>

        <section>
            <h2>Frequently Asked Questions:</h2>

            <details>
                <summary>
                    Question 1: What is Lorem Ipsum?
                </summary>
                <p>
                    Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                </p>
            </details>

            <details>
                <summary>
                    Question 2: How do I get started?
                </summary>
                <p>
                    To get started, you can follow the instructions provided in the user manual.
                </p>
            </details>

            <details>
                <summary>
                    Question 3: Can I customize the settings?
                </summary>
                <p>
                    Yes, you can customize the settings according to your preferences in the options menu.


                </p>
            </details>

            <details>
                <summary>
                    Question 4: Is there a mobile app available?
                </summary>
                <p>
                    Yes, we have a mobile app available for both iOS and Android devices. You can download it from the respective app stores.


                </p>
            </details>


            <details>
                <summary>
                    Question 5: How can I contact customer support?
                </summary>
                <p>
                    You can reach our customer support team through the contact form on our website or by calling our helpline at XXX-XXXX.
                </p>
            </details>

        </section>

        <footer>
            <p>&#169; 2024 Solanki Chetan. All rights reserved.</p>
        </footer>

    </div>

</body>

</html>

<style>
    p {
        color: blue;
    }
</style>
"""
st.html( code )
