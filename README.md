# vboxheadless-service
Use Systemd to start a Headless Virtual Box instance on system start.

## Quick install

---
dnf copr enable voor/vboxheadless-service
dnf install -y vboxheadless-service
---

## How to Use

Copy the vbox file (usually just copy the entire directory) into a folder inside `/var/lib/vboxheadless/` (created by the install), also make sure to change ownership to vboxheadless:

---
su -c 'chown vboxheadless:vboxusers -R /var/lib/vboxheadless && restorecon -R /var/lib/vboxheadless'
---

Temporarily become vboxheadless and add it to the managed VMs:

---
sudo su - vboxheadless -s /bin/bash
VBoxManage registervm /var/lib/vboxheadless/${PATH_TO_FILE}.vbox
---

Get the UUID of the resulting VM:

---
VBoxManage list vms
---

Now enable the service with the UUID:

---
systemctl enable --now vboxheadless-service@${UUID}.service
---

Check to make sure it's successfully up (or just try and remote into it):

---
systemctl status vboxheadless-service@${UUID}.service
---
