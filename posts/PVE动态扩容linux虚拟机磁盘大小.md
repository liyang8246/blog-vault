---
date: 2025-12-19
tags:
  - linux
---
仅针对 linux+gpt+ext4

1. 在 `PVE` Web 控制台给硬盘增加容量
2. 打开控制台查看文件系统情况

可以看到根目录已满

```bash
root@ubuntu:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           9.5G  1.8M  9.5G   1% /run
/dev/sda2       126G  119G  2.1G  99% /
```

3. 启动分区工具 `sudo parted /dev/sda`

```bash
root@ubuntu:~# parted /dev/sda
GNU Parted 3.6
Using /dev/sda
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted)
```

4. 查看分区 `print` 此时会提示修复 gpt 分区表, 填 Fix

```sql
(parted) print
Warning: Not all of the space available to /dev/sda appears to be used, you can fix the GPT to use all of the space (an extra 268435456 blocks) or continue with the current setting?
Fix/Ignore? Fix
Model: QEMU QEMU HARDDISK (scsi)
Disk /dev/sda: 275GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:

Number  Start   End     Size    File system  Name  Flags
 1      1049kB  2097kB  1049kB                     bios_grub
 2      2097kB  137GB   137GB   ext4/
```

5. 扩容分区, 我这里主分区 Number 是 2 , `resizepart 2 `, 提示 End? , 填 `100%`, 随后 `quit` 退出

```bash
(parted) resizepart 2
Warning: Partition /dev/sda2 is being used. Are you sure you want to continue?
Yes/No? Yes
End?  [137GB]? 100%
(parted) quit
Information: You may need to update /etc/fstab.
```

6. 重新加载分区表和扩展分区

```bash
sudo partprobe /dev/sda
sudo resize2fs /dev/sda2
```

```bash
root@ubuntu:~# sudo partprobe /dev/sda
root@ubuntu:~# sudo resize2fs /dev/sda2
resize2fs 1.47.0 (5-Feb-2023)
Filesystem at /dev/sda2 is mounted on /; on-line resizing required
old_desc_blocks = 16, new_desc_blocks = 32
The filesystem on /dev/sda2 is now 67108347 (4k) blocks long.
```

7. 查看是否生效 `df -h`

可以看到 avail 是 120G 已经扩容成功了

```bash
root@ubuntu:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           9.5G  1.6M  9.5G   1% /run
/dev/sda2       252G  122G  120G  51% /
```