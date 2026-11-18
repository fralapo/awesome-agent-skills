# Chapter 6: Scams, Security and Backup for Home Users

## Core Idea
Most home losses come from a few repeatable patterns: an offer too good to be true, a message that imitates a trusted sender, a reused weak password, a network where every device trusts every other, and data that existed in only one place. In this model defence is mostly habit and structure (verify, isolate, keep copies) rather than clever tools, and the human factor is the main weakness.

## 6.1 Hardware scams and counterfeit parts
- **Thesis**: price and seller history are evidence; a part that arrives is not proof that it is what it says.
- **Mechanism**: a counterfeit graphics card can be an old model with modified firmware so that it reports itself as a newer one. Symptoms: no boot, driver trouble that even a clean operating-system install does not cure. Unmasking: a hardware-information tool shows parameters that do not match the claim (for example a fill rate far below the real model), the circuit board does not match the sticker, the number or size of memory chips is inconsistent with the stated capacity. Report and ask for a refund including shipping. Schemes also take orders at impossible prices and disappear; positive reviews can be fake, so read the negative ones.
- **Seller checks**: many feedbacks for cheap items followed by an expensive one is suspicious; for a new seller use a payment method with buyer protection; ask for photos of front and back and proof that it works; stop if anything does not fit. On a large marketplace, protection is fullest for items sold and shipped by the platform itself and weaker for third-party sellers.
- **Trade-off**: verification takes minutes and costs the deal if the seller refuses.
- **Does not hold when**: the seller is an established shop with a return policy.

## 6.2 Cheap computers and preinstalled software
- **Thesis**: a very cheap mini PC is cheap for a reason, and the operating system on it cannot be trusted.
- **Mechanism**: reported cases of modified system images with preinstalled non-standard programs, installation without online activation, hidden folders with scripts, and files flagged as backdoors by scanners. Many brands are relabelled copies of a few designs. Countermeasures: wipe the drive including all partitions and reinstall from official media on a clean machine, run scans, and keep the device on an isolated network segment until trusted. Other cheap-hardware limits: power brick and heat, soldered memory and storage, outdated firmware. Wildly low power claims on gadgets (a USB fridge) point to a limit of the port, not a trick.
- **Trade-off**: reinstalling costs an hour.
- **Does not hold when**: the machine comes from a vendor with signed, documented images.

## 6.3 Phishing, one-time codes and fake messages
- **Thesis**: attackers imitate a trusted body to steal credentials and then the one-time code.
- **Mechanism**: a site copied from the original asks for a login, then for the code that arrives by message. Signals: a generic greeting or one about a product you do not own, urgency, a request to click and "update your details", a sender domain that is slightly off. Do not click or open attachments; contact the body through channels you find yourself and not the ones in the message. The same applies to text messages, phone calls and game accounts. If you are a victim, change passwords, enable multi-factor authentication, report it to the authorities. Password hygiene is in `computer-science-fundamentals` ch9.8 (unique passwords, a manager, passkeys).
- **Trade-off**: slower response time to real notices.
- **Does not hold when**: the message is a login prompt you initiated yourself on a verified address.

## 6.4 Ransomware: entry, effect and defence
- **Thesis**: ransomware encrypts your files and demands a payment; it is not the same as a data breach, and payment is no guarantee.
- **Mechanism**: entry usually comes from a weak or reused password, an executable attachment disguised as an invoice, a shared or aggregated connection with a compromised user, or an exposed router or remote-access service. Once inside a flat home network it finds shared drives and other machines. Some strains encrypt only certain file types or start from certain folders, which limits damage by luck. Payment funds crime and may not restore data. If hit: disconnect from the network, change passwords, enable multi-factor authentication, tell those affected, keep the encrypted files (a flaw in the malware may later allow free decryption; public projects list known decryptors), and see the backup rules in 6.6. Dated, reported example: a flaw (one keystream reused across files) allowed recovery, years later, of files encrypted by one strain, which shows why keeping the encrypted copy can pay off.
- **Trade-off**: segmentation and backups cost setup time.
- **Does not hold when**: the attacker also holds the backups, which is why one copy must be offline.

## 6.5 Network hygiene: isolate what you cannot trust
- **Thesis**: assume some device will be compromised and limit what it can reach.
- **Mechanism**: printers, cameras and smart devices often ship with default credentials, a weak direct-connection mode and web panels that reveal the main network's password; change every default, update firmware, turn off the router's push-button setup feature, use the newest wireless security mode and a long passphrase, and place such devices on a separate segment (a VLAN) that can reach only the Internet. A determined attacker can still pivot between segments. Wireless attacks demonstrated in tutorials (deauthenticating a client to capture a handshake and guessing offline with a word list, forging a look-alike access point) work against weak passphrases and personal-information word lists; test only your own network or with permission. A DNS-level blocker on the network drops ad, tracking and phishing domains for every device but is not infallible. A virtual private network hides traffic from the local network and the access provider, not from the VPN operator; free ones are poor and an encrypted web connection already protects most content (position).
- **Trade-off**: segmentation takes hardware and learning; some smart devices stop working.
- **Does not hold when**: a single trusted device is the only thing on the network.

## 6.6 Backup principles
- **Thesis**: a backup is a copy you have restored successfully; everything else is hope.
- **Mechanism**: redundancy (RAID, mirroring) keeps a service up after a drive failure but replicates deletion, corruption and encryption instantly, so it is not a backup. The 3-2-1 rule: three copies, on two kinds of media, one off site. Snapshots roll back changes, but not past the retention window or to files created after the snapshot, and live on the same system; keep at least one copy offline or immutable so ransomware cannot reach it. Encrypt remote copies on your side and keep the key offline. Schedule the job, test a restore regularly and time it. Keep the old system image and a boot-and-repair stick for recovery, since reinstalling is usually faster than diagnosing a damaged system. Surge and outage protection (chapter 1) is part of the same plan.
- **Trade-off**: storage and attention costs against catastrophic loss.
- **Does not hold when**: the data can be recreated cheaply, in which case spend nothing.

## 6.7 Processor-level flaws, trusted modules and operating-system myths
- **Thesis**: some flaws are in the hardware design; judge them by your threat model.
- **Mechanism**: speculative execution lets a processor run ahead before access checks complete; side channels reveal what it touched. A kernel-memory flaw is mitigated in software by separating address spaces, at a performance cost that depends on how often the workload crosses the kernel boundary (reported ranges from a few percent in normal use to much more in kernel-heavy loads); later variants (branch-history based) are mitigated partially, and real fixes are in hardware. For an ordinary user the risk is lower than for a shared server, and declining a patch for a few frames is a poor trade (position). A trusted platform module is a small component that stores keys and releases them only if the machine is in an expected state; it concentrates trust in one part and has had bugs; it is distinct from secure boot, and a requirement can be bypassed by users. A research attack that turned a graphics card's memory clock into radio signals needed prior compromise and is a curiosity for most people (position).
- **Operating-system facts**: a driver is the layer between the operating system and a component; it runs with high privilege, so a faulty driver can halt the machine. Shutdown stops users, programs and services and then asks the hardware to power off through the firmware interface; "fast startup" is a partial hibernation and a restart begins from scratch. A system image or a live recovery environment beats diagnosis. Gaming on other systems: a Linux distribution is built around the kernel; compatibility layers run many titles, but kernel-level anti-cheat often blocks play; status changes, so check before buying.
- **Trade-off**: patches cost speed; skipping them costs exposure.
- **Does not hold when**: the machine is offline and handles nothing sensitive.

## Common Mistakes
- Treating RAID or a single snapshot as a backup.
- Clicking through a message instead of contacting the sender independently.
- Leaving default credentials on printers and cameras.
- Paying a ransom before preserving the encrypted files.

## Checklist
- [ ] Unique passwords, a manager, multi-factor authentication?
- [ ] Untrusted devices on an isolated segment?
- [ ] 3-2-1 copies, one offline, restore tested?
- [ ] Used or cheap hardware verified and reinstalled clean?

## Connects To
ch01 (power protection), ch05 (used and marketplace purchases); `computer-science-fundamentals` ch8-9 (hashes, passwords, protocols, provenance) and ch7 (networks); `coding-with-agents` ch06 (agent safety and backups).
