B
    1\a]�  �               @   st  d dl Z d dlZdd� Zedk�rpyDd dlmZ d dlZd dlZd dlZd dlZd dl	T d dl
mZ W n ek
r�   ed� Y nX G d	d
� d
�Zy�e�  ed�Zes�ed� e� s�ed� ed� e�d� ed�Zes�ed� e�d� ede � ed� xLed�Zedk�r8ed�Zed�Ze�d� ed� nedk�re�  �qW W n ek
�rn   ed� Y nX dS )�    Nc              C   s8   d} d}x*t d�D ]}|| t�t�� d � 7 }qW |S )N�
0123456789� �   �
   )�range�mathZfloor�random)ZdigitsZOTP�i� r
   �pro.py�generateOTP   s
    r   �__main__)�tqdm)�*)�BeautifulSoupz3[1;31m[[1;36m![1;31m][1;32mPlease Root hp kamu!c               @   s$   e Zd Zdd� Zdd� Zdd� ZdS )�Payuc             C   s�   t �� | _| j�d� | j�d� | j�d� | j�d� | j�d� | jjt j	�
� dd� ddddd	d
ddddddg| j_d| _| ��  d S )NTF�   )Zmax_time)Z
Connectionz
keep-alive)ZPragmazno-cache)zCache-Controlzno-cache)ZOriginzhttp://sms.payuterus.biz)zUpgrade-Insecure-Requests�1)zContent-Typez!application/x-www-form-urlencoded)z
User-AgentzVOpera/9.80 (Android; Opera Mini/8.0.1807/36.1609; U; en) Presto/2.12.423 Version/12.16)ZAcceptzvtext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3)ZRefererzhttp://sms.payuterus.biz/alpha/)zAccept-Encodingzgzip, deflate)zAccept-Languagez#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7)ZCookiezn_ga=GA1.2.131924726.1560439960; PHPSESSID=jjrqqaakmfcgfgbtjt8tve5595; _gid=GA1.2.1969561921.1561024035; _gat=1zhttp://sms.payuterus.biz/alpha/)�	mechanizeZBrowser�brZset_handle_equivZset_handle_gzipZset_handle_redirectZset_handle_refererZset_handle_robotsZset_handle_refreshZ_httpZHTTPRefreshProcessorZ
addheaders�u�banner)�selfr
   r
   r   �__init__   s*    

zPayu.__init__c             C   s^   t �d� td� td� td� td� td�}td� t�d� d	t�  }| �||� d S )
N�clearuN   [1;32m	 ╦ ╦╦ ╦╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗	uN   [1;37m	 ║║║╠═╣╠═╣ ║ ╚═╗╠═╣╠═╝╠═╝	u>   [1;32m	 ╚╩╝╩ ╩╩ ╩ ╩ ╚═╝╩ ╩╩  ╩	z)[5;37;42m	WhatsApp on CLI by Khazul	[0mu5   
[1;32m[[1;31m√[1;32m][1;33mNomor kamu:[1;36m u9   [1;32m[[1;31m√[1;32m][1;33mSedang mengirim kode OTP�   z)WhatsApp on CLI by Khazul
Your OTP code: )�os�system�print�input�time�sleepr   �main)r   �no�psnr
   r
   r   r   )   s    


zPayu.bannerc             C   s�   g }t | j�| j�dd�}x|�d�D ]}|�|j� q&W tt|�d �tt|�d � }| jj	dd� || jj
d< || jj
d	< t|�| jj
d
< | j�� �� }dt|�kr�td| � n.dt|�kr�td� t��  ntd� t��  d S )Nzhtml.parser)Zfeatures�spanr   �   r   )ZnrZnohpZpesanZcaptchazSMS Gratis Telah Dikirimu@   [1;32m[[1;31m√[1;32m][1;33mKode OTP kamu sudah dikirim ke zMohon Tunggu 8 Menit LagiuR   [1;32m[[1;31m√[1;32m][1;33mTunggu 8 menit untuk mengirim ulang kode OTP kamuu>   [1;32m[[1;31m√[1;32m][1;33mKode OTP kamu gagal terkirim!)�BSr   �openr   Zfind_all�append�text�int�strZselect_formZformZsubmit�readr   �sys�exit)r   r#   �msg�oZbs�xZcapt�subr
   r
   r   r"   4   s"     
z	Payu.mainN)�__name__�
__module__�__qualname__r   r   r"   r
   r
   r
   r   r      s   r   z4
[1;31m[[1;32m+[31m][1;33mKode OTP kamu:[1;36m z$[!][1;31mPlease input kode OTP kamuz[!][1;31mKode OTP kamu salahuC   
[1;35m[[1;36m√[1;35m][1;37mPlease wait for login WhatsApp...�   u:   [1;35m[[1;36m√[1;35m][1;37mTambah nama kamu:[1;33m z [!][1;31mPlease input nama kamuu<   [1;35m[[1;36m√[1;35m][1;37mSelamat datang di WhatsApp u4   
[1;34m[[1;35m×[1;34m][1;31mNo message in here!z<
[1;36m[[1;31m+[1;36m][1;37mMau KIRIM pesan atau TIDAK? ZKIRIMz,[1;36m[[1;31m+[1;36m][1;37mKetik nomor: z([1;36m[[1;31m+[1;36m][1;37mPesan:
> u6   [1;34m[[1;31m√[1;34m][1;36mPesan Gagal terkirim!ZTIDAKz[!]GoodByee...)r   r   r   r4   r   r   r    r   r.   ZwebwhatsapiZbs4r   r'   �ImportErrorr/   r   r   Zotpr   r!   �nameZulZtambahr$   �KeyboardInterruptr
   r
   r
   r   �<module>   sH   
 8





