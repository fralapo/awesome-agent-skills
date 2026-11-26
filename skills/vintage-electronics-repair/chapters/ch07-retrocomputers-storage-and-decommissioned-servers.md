# Chapter 7: Retrocomputers, Storage and Decommissioned Servers

## Core Idea
Old computers fail in a few repeatable ways: a dead backup battery, oxidised contacts, bulged capacitors, a failing disk, an exhausted power supply, and a configuration that was never written down. In this model the first duty is to protect the data, the second to restore power and contacts, and the third to deal with software and drivers of the period. Hardware of this kind is also a privacy matter, because it may hold someone else's records.

## 7.1 Protect the data first
- **Principle**: Any repair step can destroy the only copy of the data, so copy before you change.
- **How it works / sequence**: Image the system disk (sector by sector) onto other storage before testing, repairing the operating system or changing a RAID; work from the copy.
- **Moves**:
  - Clone with a partitioning or imaging tool; in a server, the controller decides the boot disk, so remove the source disk or set the boot device accordingly.
  - Repairing an operating system "in place" is risky without a copy; do it only after imaging.
  - Deleting and recreating a RAID without a clone loses the data.
  - Machines in a kiosk configuration may be defended against change; an image lets you experiment safely.
  - Tape backup software can erase the files on the tape; read the documentation.
- **Evidence**: Practitioner
- **Trade-off**: Imaging takes time and storage and avoids irreversible loss.
- **Does not hold when**: The disk is failing so badly that reading it more damages it; then specialist recovery.

## 7.2 No power, no boot: the ordered checklist
- **Principle**: A machine that does not start has a short list of causes, in a definite order.
- **How it works / sequence**: Check the mains and fuse, then the supply rails (3.3 V, 5 V, 12 V) with a meter, then the backup battery, then memory and cards, then the board.
- **Moves**:
  - A dead supply can resume with a replaced filter capacitor; test with a limited load.
  - Remove cards and memory modules one at a time, reseat the rest, and clean the contacts of memory, processor sockets, expansion slots and cards.
  - A supply that starts without load but shuts down under load is a faulty or undersized supply.
  - Run a memory test for several hours before trusting a system.
  - Bulged or exploded capacitors on boards are replaced; check that nearby traces are intact.
  - Mind jumpers: a jumper moved to the wrong voltage position on a card can blow a fuse.
- **Evidence**: Practitioner
- **Trade-off**: Systematic checks are slow and prevent damage.
- **Does not hold when**: The board shows physical damage that outranks all other causes.

## 7.3 The backup battery and clock memory
- **Principle**: The cell that keeps the configuration and clock is a classic cause of strange symptoms.
- **How it works / sequence**: Measure the cell; replace it if it is low or has leaked; clean corrosion; restore the configuration and check that the system sees its disks.
- **Moves**:
  - Symptoms include a disk not recognised, memory errors, lost settings, a keyboard that stutters, a BIOS that loses its settings or becomes corrupt, and random restarts.
  - Soldered or embedded cells (inside a clock chip) can be bypassed with an external holder, taking care at the chip pins; follow the datasheet.
  - A series diode may protect against recharging a primary cell; do not remove it.
  - After reinstalling or resetting a BIOS, check for settings that block boot.
- **Evidence**: Practitioner
- **Trade-off**: External cell holders alter the original.
- **Does not hold when**: The failure is in the chip itself.

## 7.4 Storage: disks, controllers, RAID and removable media
- **Principle**: Old storage interfaces have rules about IDs, termination and cables that are easy to violate.
- **How it works / sequence**: Set unique IDs for SCSI devices, use proper termination and cables, connect disks to one controller, and check what each controller can read.
- **Moves**:
  - Overlapping SCSI IDs cause chaos in disk sets.
  - SATA disks work on SAS controllers but not the reverse.
  - A RAID volume may not be movable to another controller; know the controller before migrating.
  - Removing a disk from a live RAID leaves it degraded but accessible; rebuild afterwards.
  - Small flash cards on adapters can replace old disks for older machines; the capacity and geometry may be limited by the BIOS.
  - Floppy emulators and modern floppy-compatible devices exist; forcing a drive to see a different density sometimes means cutting or covering a sense hole or tracing a switch.
  - Old tape cartridges and rare drives (quarter-inch cartridge, zip disks) may have no documentation; a drive that stays silent after all jumper combinations is a sign to stop.
- **Evidence**: Practitioner
- **Trade-off**: Modern storage replacements are reliable; period devices are authentic.
- **Does not hold when**: Original media is the point of preservation.

## 7.5 Operating systems, drivers and period software
- **Principle**: Old cards and applications are bound to old operating systems.
- **How it works / sequence**: Pick the OS version the hardware was made for; check driver availability before you build a system; use virtual machines or emulators when the hardware is not essential.
- **Moves**:
  - Some cards install only under a particular version; newer versions refuse their drivers.
  - A graphics card with stuttering overlay may be replaced with a more compatible one.
  - Passwords on old systems can be reset with a live USB; unencrypted disks can be read on another machine. Do this only for equipment you are entitled to access (chapter 2).
  - Disk images can be converted to formats that emulators read; emulators run on small boards.
  - Applications stored in proprietary databases can have password fields in a table.
- **Evidence**: Practitioner
- **Trade-off**: Period software is authentic and fragile.
- **Does not hold when**: Virtualisation is enough for the task.

## 7.6 Mid-age PCs, graphics cards and platform quirks
- **Principle**: Late-generation hardware repair is bench micro-work: pins, solder balls, thermal limits.
- **How it works / sequence**: Inspect sockets with magnification; straighten bent pins carefully; reflow or re-solder lifted parts with flux; test with stress tools after the repair; check cooling.
- **Moves**:
  - Dual BIOS switches rescue a failed flash.
  - A graphics card that shows an error code on a new platform may need a BIOS image with the correct identifiers; use the manufacturer's tool and the matching image.
  - Fan curves and power limits matter in small systems.
  - A processor reporting very high temperature with liquid cooling may have air in the loop.
  - External graphics via different cable standards trades bandwidth against convenience; a faulty cable can mislead the whole test.
  - Unlocking turbo behaviour on a portable machine increases heat; watch the temperature.
- **Evidence**: Practitioner
- **Trade-off**: Micro-repair saves a board and needs patience, tools and microscopes.
- **Does not hold when**: The board is cracked or corroded under chips.

## 7.7 Servers and render farms
- **Principle**: Decommissioned servers are cheap hardware with unusual boot, memory and power rules, and power draw and heat scale with the number running.
- **How it works / sequence**: Identify the platform, memory type (ECC), controller, remote-management port and power supply; flash, update or reset where documented; run a full memory test; then load-test.
- **Moves**:
  - Server memory is often ECC and registered; ordinary memory may not work.
  - Some older servers draw well over a hundred watts at idle; add up the draw before plugging many into one circuit. Running many machines together can exceed a home circuit and trip it; stagger switch-on and check the room temperature.
  - A chassis bent in transport can be straightened, with care.
  - A raid or software cluster needs a shared network configuration (static addresses, name resolution, shares).
  - Consider the value: the used price of a server is low, and its running cost may exceed its usefulness.
- **Evidence**: Practitioner; Position for the economics.
- **Trade-off**: Servers offer many cores and RAM for little money, with noise, heat and electricity cost.
- **Does not hold when**: A single modern machine does the same job at lower power.

## 7.8 Salvaged machines and other people's data
- **Principle**: Recovered computers can carry business and personal information.
- **How it works / sequence**: Decide before powering on how you will treat what you find: do not publish it, return it if the owner asks, wipe it before resale.
- **Moves**:
  - An owner may ask for data to be deleted and for the machine not to be sold; honour it.
  - Be careful with dumpster-sourced machines: they may carry a fault that was the reason they were thrown away.
  - Disks destroyed by the former owner should not be assumed readable.
- **Evidence**: Position
- **Trade-off**: Ethical handling reduces options for resale.
- **Does not hold when**: The data is yours.

## 7.9 Static, handling and moving machines
- **Principle**: Discharge static and avoid hazards that old equipment makes worse.
- **How it works / sequence**: Touch the grounded chassis before handling cards; avoid using static to test; lift heavy cases with help; keep toner out of your lungs with a filtered vacuum if you clean printers.
- **Moves**:
  - Bags and mats protect boards.
  - Do not operate on the system while the supply is connected unless the design requires it.
- **Evidence**: Practitioner
- **Trade-off**: Careful handling is cheap.
- **Does not hold when**: The task is non-electrical.
