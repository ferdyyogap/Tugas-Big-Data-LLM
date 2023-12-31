import streamlit as st
import google.generativeai as palm
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

API_KEY = os.environ.get("PALM_API_KEY")
palm.configure(api_key=API_KEY)

def main():
  st.header("Surat Lamaran AI ✍️")
  st.write("")

  # Personal information
  full_name = st.text_input("Name:")
  address = st.text_input("Address:")
  email = st.text_input("email:")
  phone_number = st.text_input("Phone Number:")

  # Company information
  company_name = st.text_input("Company Name:")
  company_address = st.text_input("Company Address:")
  hr_name = st.text_input("HR Name:")

  # Position applied
  position_applied = st.text_input("Position Applied:")

  # Background
  background = st.text_input("Background:")

  # Experience
  experience = st.text_input("Experience:")

  # Skills
  skills = st.text_input("Skills:")

  date = datetime.date.today()

  if st.button("Generate Cover Letter", use_container_width=True):
    model = "models/text-bison-001"  # This is the currently available model

    prompt = f"""
  Address: {address}
  Date: {date}
  {hr_name}
  {position_applied}
  {company_name}
  {company_address}

  Dear {hr_name},

  I am writing to express my interest in the {position_applied} position at {company_name}, which I saw advertised on your company website.

  I have a background in {background} and {experience}. I also have the skills of {skills}.

  Here is a brief summary of my qualifications:
  Name: {full_name}
  Address: {address}
  Email: {email}
  Phone Number: {phone_number}

  I am very interested in joining {company_name} because I admire the company's achievements in developing innovative AI solutions. I am confident that with my background and skills, I can make a valuable contribution to the team.

  I have attached my resume, which provides more details about my work experience and education. I am very eager to have the opportunity to meet with you in an interview to discuss further how I can add value to {company_name}.

  Thank you for your time and consideration. I look forward to joining your great team soon.

  Sincerely,
  {full_name}
  """

    response = palm.generate_text(
      model=model,
      prompt=prompt,
      max_output_tokens=1500  # Adjust as needed for longer letters
    )

    st.write("")
    st.header(":blue[Surat Lamaran]")
    st.write("")

    st.markdown(response.result, unsafe_allow_html=False, help=None)

if __name__ == "__main__":
  main()
