All commands were tested on a Ubuntu 24.04 LTS. If you choose to use another distribution, you might need to check appropriate commands to get the same result. 

1. Have access to an unrestricted Ubuntu server.
I got mine from https://www.digitalocean.com but you can use other providers as long as they don’t have extra firewall configuration that may interfere with this demo.

3. You will need to have root access
4. To be able to do the DNS configuration part, you also need to have a domain purchased in advance.

If you opt in to use DigitalOcean option: 
- you may want to request the account a few days prior to this course, as it needs a manual validation in activation the account.

1. Go to https://cloud.digitalocean.com/ and from top right, select "Create Droplets"
   ![image](https://github.com/user-attachments/assets/1de2210a-6285-409f-a103-5fdcf09e9257)
2. Select a region - ideally a DC closest to your region
3. Choose an image - in this demo we will be using Ubuntu 24.04 (LTS) x64
  ![image](https://github.com/user-attachments/assets/a606bb6a-b521-4387-ab5b-56e650d43f2e)

4. Choose size of the VM: BASIC
5. Choose CPU Options - Type regular:
![image](https://github.com/user-attachments/assets/fd48f45a-13dd-46b8-8e08-aa24e392b3c0)

6.  Pick a rate - I tested with following config, but cheapest option should also work fine. 
![image](https://github.com/user-attachments/assets/a1422739-b3eb-4393-9371-c4eca2d74f64)

prometheus
1 GB Memory / 25 GB Disk / AMS3 - Ubuntu 24.04 (LTS) x64

7. Choose as authentication method: **password** and create a password that you will remember/ note it down, you will need it in the lesson.
8. In the lower section of the page, give a Hostname to your VM
9. Create and review its state under Resources section:
![image](https://github.com/user-attachments/assets/1fd30132-70b8-4319-aa13-1633d5de0a5e)


   

