from PIL import Image
import streamlit as st
import pack as pk
import steganography_package as sp
import otpgen as otp
import blowfish as bl
import railfence as rf
import sound_file as sf
import rgb as rgb
import gray as gr
import Logistic as lg


def load_image(image_file):
	img = Image.open(image_file)
	return img

def main():
    st.title("Security Package")
    menu=["Steganography","Encryption and Decryption","Background Removal","OTP Authentication","Audio Encryption","Audio Decryption","Image Encryption and Decryption"]


    choice=st.sidebar.selectbox("MENU",menu)

    if choice=="Steganography":
        st.subheader("Steganography")
        option = st.selectbox('Which Operation you want to perfrom:',('Encryption','Decryption'))
        if option=='Encryption':
            img=st.text_input("Enter the path to the input image file: ")
            st.text(img)

            txt=st.text_input("Enter the data to be encoded into the image")

            st.text(txt)
        
            op_image_name=st.text_input("Enter the name of new image(with extension)")

            st.text(op_image_name)

            if img and txt and op_image_name:
                st.image(load_image(img),width=500,caption="Original Image")
                image_file=Image.open(img)
                new_image=sp.encode(image_file,txt)
                st.image(new_image,width=500,caption="New Image")
                st.image(new_image,width=500,caption="Encoded Image")
                new_image.save(op_image_name, str(op_image_name.split(".")[1].upper()))
        elif option=='Decryption':
            img=st.text_input("Enter the path to the Encrypted image file: ")
            st.text(img)

            if img:
                st.image(load_image(img),width=500,caption="Encrypted Image")
                image_file=Image.open(img)
                decrypted_text = sp.decode(image_file)
                st.subheader("Message Retrieved from the File : "+decrypted_text)
    
    
    elif choice=='Encryption and Decryption':
        option = st.selectbox('Select the Cipher',('Caesar','Monoalphabetic','Transpositional'))
        txt_path = st.text_input("Enter the path to the text file")
        st.text(txt_path)
        # txt_path = Path(txt_path_full)
        # st.text(txt_path)
        if txt_path!='.':
            f1 = open(txt_path,'r')
            file_content = f1.read()
            f1.close()
        ch = st.selectbox('Choose the Operation',('Encryption','Decryption'))
        li = []
        if ch=='Encryption' and option =='Caesar' and txt_path:
            key = st.text_input("Enter the key for encrypting in Caesar Cipher")
            final_content=pk.caesaren(file_content,key)
            f2=open(txt_path,'w')
            f2.write(final_content)
            f2.close()
            st.subheader("Encryption Successful!! Check your File")
        
        if ch=='Decryption' and option =='Caesar' and txt_path:
            key = st.text_input("Enter the key for decrypting in Caesar Cipher")
            final_content=pk.caesarde(file_content,key)
            f2=open(txt_path,'w')
            f2.write(final_content)
            f2.close()
            st.subheader("Decryption Successful!! Check your File")
        
        if ch=='Encryption' and option =='Monoalphabetic' and txt_path:
            final_content=pk.monoalphen(file_content)
            f2=open(txt_path,'w')
            f2.write(final_content)
            f2.close()
            st.subheader("Encryption Successful!! Check your File")
        
        if ch=='Decryption' and option =='Monoalphabetic' and txt_path:
            final_content=pk.monoalphde(file_content)
            f2=open(txt_path,'w')
            f2.write(final_content)
            f2.close()
            st.subheader("Decryption Successful!! Check your File")

        if ch=='Encryption' and option =='Transpositional' and txt_path:
            key=st.text_input("Enter the key for Transpositional Encryption")
            l = list(key)
            if key!='':
                final_content,l=pk.transposen(file_content,l)
                f2=open(txt_path,'w')
                f2.write(final_content)
                f2.close()
                st.subheader("Encryption Successful!! Check your File")
                f3=open("keyfile.txt",'w')
                f3.write(l[0])
                f3.write(l[1])
                f3.close()
            final_content,l=pk.transposen(file_content,l)
            f2=open(txt_path,'w')
            f2.write(final_content)
            f2.close()
            st.subheader("Encryption Successful!! Check your File")
            f3=open("keyfile.txt",'w')
            f3.write(l[0])
            f3.write(l[1])
            f3.close()

        if ch=='Decryption' and option =='Transpositional' and txt_path:
            # key=st.text_input("Enter the key for Transpositional Decryption")
            # l = list(key)
            f4 = open("keyfile.txt",'r')
            li=[]
            li.append(f4.read())
            key_decry = []
            key_decry.append(li[0][0])
            key_decry.append(li[0][1])
            st.text(key_decry)
            final_content=pk.transposde(file_content,key_decry)
            f2=open(txt_path,'w')
            f2.write(final_content)
            f2.close()
            st.subheader("Decryption Successful!! Check your File")

        
        if ch=='Encryption' and option =='Playfair' and txt_path:
            key = st.text_input("Enter the key for encrypting in Playfair Cipher")
            if key!='':
                final_content=pk.playfairen(file_content,key)
                f2=open(txt_path,'w')
                f2.write(final_content)
                f2.close()
                st.subheader("Encryption Successful!! Check your File")

        if ch=='Decryption' and option =='Playfair' and txt_path:
            key = st.text_input("Enter the key for decrypting in Playfair Cipher")
            if key!='':
                final_content=pk.playfairde(file_content,key)
                f2=open(txt_path,'w')
                f2.write(final_content)
                f2.close()
                st.subheader("Decryption Successful!! Check your File")

        
        if ch=='Encryption' and option =='Hill' and txt_path:
            key = st.text_input("Enter the key for encrypting in Hill Cipher")
            if key!='':
                final_content=pk.Hillen(file_content,key)
                f2=open(txt_path,'w')
                f2.write(final_content)
                f2.close()
                st.subheader("Encryption Successful!! Check your File")

        if ch=='Decryption' and option =='Hill' and txt_path:
            key = st.text_input("Enter the key for decrypting in Hill Cipher")
            if key!='':
                final_content=pk.Hillde(file_content,key)
                f2=open(txt_path,'w')
                f2.write(final_content)
                f2.close()
                st.subheader("Decryption Successful!! Check your File")

        if ch=='Encryption' and option =='Blowfish' and txt_path:
            #key = st.text_input("Enter the key for encrypting in Hill Cipher")
            fc = int(file_content)
            final_content=bl.encrypt(fc)
            f2=open(txt_path,'w')
            f2.write(str(final_content))
            f2.close()
            st.subheader("Encryption Successful!! Check your File")
        
        if ch=='Decryption' and option =='Blowfish' and txt_path:
            #key = st.text_input("Enter the key for encrypting in Hill Cipher")
            fc = int(file_content)
            final_content=bl.decrypt(fc)
            f2=open(txt_path,'w')
            f2.write(str(final_content))
            f2.close()
            st.subheader("Decryption Successful!! Check your File")

        if ch=='Encryption' and option =='Railfence' and txt_path:
            key = st.text_input("Enter the key for encrypting in Railfence Cipher")
            if key!='':
                final_content=rf.railfenceen(file_content,int(key))
                f2=open(txt_path,'w')
                f2.write(final_content)
                f2.close()
                st.subheader("Encryption Successful!! Check your File")

        if ch=='Decryption' and option =='Railfence' and txt_path:
            key = st.text_input("Enter the key for decrypting in Railfence Cipher")
            if key!='':
                final_content=rf.railfencede(file_content,int(key))
                f2=open(txt_path,'w')
                f2.write(final_content)
                f2.close()
                st.subheader("Decryption Successful!! Check your File")
        


    elif choice=='OTP Authentication':
        reciever_email=''
        value=0
        reciever_email=st.text_input("Enter the email to which OTP should be sent")
        if reciever_email!='' and value==0:
            value=otp.otpgenerator(reciever_email)
        if value!=0:
            st.text("OTP Sent to the Email Address")
            auth=''
            auth = st.text_input("Enter the OTP for Authentication")
            # st.text(value)
            # st.text(auth)
            if auth:
                k=int(auth)
                if k == value:
                    st.subheader("OTP Verified!!")
                else:
                    st.subheader("OTP Authenticated!! Continue")
    elif choice=="Audio Encryption":
        aud=st.text_input("Enter the path to the Audio file to be encrypted: ")
        st.text(aud)
        
        if aud:
            sf.audio_encryption(aud)
            st.subheader("Audio File is Encrypted!!\nCheck Your Users Folder to find the Encrypted Audio File")
    elif choice=="Audio Decryption":
        aud=st.text_input("Enter the path to the Audio file to be decrypted: ")
        st.text(aud)
        a_key=st.text_input("Enter the path to the key file for Decrypting the audio file: ")
        st.text(a_key)
        
        if aud and a_key:
            sf.audio_decryption(aud,a_key)
            st.subheader("Audio File is Decrypted!!\nCheck Your Users Folder to find the Decrypted Audio File")


    elif choice=='Image Encryption and Decryption':
        opt1 = st.selectbox('Select the Algorithm',('Lorenz','Logistic','RGB'))
        opt2 = st.selectbox('Which Operation you want to perfrom:',('Encryption','Decryption'))
        if opt1=="Lorenz" and opt2 == "Encryption":
            p = st.text_input("Enter the path to the Image file to be encrypted: ")
            x = st.text_input("Enter key1 ")
            y = st.text_input("Enter key2 ")
            z = st.text_input("Enter key3 ")
            if p and x and y and z:
                gr.greyen(p,x,y,z)
                st.subheader("Image File is Encrypted!!\nCheck Your Users Folder to find the Encrypted File")
        
        if opt1=="Lorenz" and opt2 == "Decryption":
            p = st.text_input("Enter the path to the Image file to be Decrypted: ")
            x = st.text_input("Enter key1 ")
            y = st.text_input("Enter key2 ")
            z = st.text_input("Enter key3 ")
            if p and x and y and z:
                gr.greyde(p,x,y,z)
                st.subheader("Image File is Decrypted!!\nCheck Your Users Folder to find the Decrypted File")
        
        if opt1=="Logistic" and opt2 == "Encryption":
            p = st.text_input("Enter the path to the Image file to be encrypted: ")
            x = st.text_input("Enter key1 ")
            y = st.text_input("Enter key2 ")
            if p and x and y:
                lg.logisticen(p,float(x),float(y))
                st.subheader("Image File is Encrypted!!\nCheck Your Users Folder to find the Encrypted File")
        if opt1=="Logistic" and opt2 == "Decryption":
            p = st.text_input("Enter the path to the Image file to be decrypted: ")
            x = st.text_input("Enter key1 ")
            y = st.text_input("Enter key2 ")
            if p and x and y:
                lg.logisticde(p,float(x),float(y))
                st.subheader("Image File is Decrypted!!\nCheck Your Users Folder to find the Decrypted File")
        if opt1=="RGB" and opt2 == "Encryption":
            rgb_str = st.text_input("Enter the String to be converted to RGB Image ")
            x = st.text_input("Enter the key ")
            if rgb and x:
                rgb.rgben(rgb_str,int(x))
                st.subheader("String is converted into RGB File!!\nCheck Your Users Folder to find the Encrypted File")
        if opt1=="RGB" and opt2 == "Decryption":
            p = st.text_input("Enter the path to the Image file to be decrypted: ")
            x = st.text_input("Enter the key ")
            if p and x:
                ret_str = rgb.rgbde(p,int(x))
                if ret_str:
                    st.text(ret_str)   




        
        # if opt1=="Logistic" and opt2 == "Encryption":
        # if opt1=="Logistic" and opt2 == "Decryption":


    # elif choice=="Background Removal":
    #     bg.bgrem()


        














    # image_file = st.file_uploader("Upload the image where the text has to be encoded", type=["png","jpg","jpeg"])

    # st.write(type(image_file))

    


    



if __name__=="__main__":
    main()