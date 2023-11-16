import streamlit as st

def main():
    st.title("crud operation")
    option = st.sidebar.selectbox("Select an operation",("Create","Read","Update","Delete"))
    if option=="Create":
        st.subheader("Create a record")
        u_name=st.text_input("Enter name")
        email=st.text_input("Enter Email")
        if st.button("Create"):
            sql="insert into users(u_name,email)values(%s,%s)"
            val=(u_name,email)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Created Successfully")

    elif option=="Read":
        st.subheader("Read Record")
        mycursor.execute("select*from users")
        result =mycursor.fetchall()
        for row in result:
            st.write(row)


    elif option=="Update":
        st.subheader("Update Record")
        id=st.number_input("Enter ID",min_value=1)
        u_name=st.text_input("Enter name to update")
        email=st.text_input("Enter Email to update")
        if st.button("Update"):
            sql="Update users set u_name=%s, email =%s where id=%s"
            val=(u_name,email,id)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record updated")




    elif option=="Delete":
        st.subheader("Delete Record")   
        id=st.number_input("Enter Id to Delete")
        if st.button("Delete"):
            sql="delete from users where id =%s"
            val=(id,)  
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record deleted")  

        

if __name__ == "__main__":
    main()
