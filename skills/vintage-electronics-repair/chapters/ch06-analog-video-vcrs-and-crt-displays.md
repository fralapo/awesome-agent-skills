# Chapter 6: Analog Video, VCRs and CRT Displays

## Core Idea
Analog video machines are tape transports with a rotating head drum, a servo and a protection logic, and the displays that go with them are tube sets with high-voltage stages. In this model the diagnosis follows the signal: sensors and protection first (a machine that stops itself is usually reacting to something), then the tape path, then the video electronics, then the display. Preservation work (transferring tapes) adds a layer of time-base correction, capture hardware and cleaning. CRT sets and tube high-voltage stages are for qualified technicians (chapter 2).

## 6.1 Protection circuits and sensors
- **Principle**: A video recorder shuts down when a sensor reports something wrong, and a faulty sensor produces the same symptom as a real jam.
- **How it works / sequence**: Observe when the machine stops (at load, at play, at rewind); trace the sensor chain in the service manual; look at sensor signals on an oscilloscope.
- **Moves**:
  - Tape-end and tape-presence sensors use LEDs and phototransistors; one line showing a clean square wave while the other shows almost nothing points at the phototransistor.
  - Intermittent sensors can be provoked with a cooling spray.
  - A temporary jumper that bypasses a sensor lowers safety margin and should be only a diagnostic step.
  - Broken optical sensor cables cause auto-eject.
- **Evidence**: Practitioner
- **Trade-off**: Bypassing finds a fault quickly but leaves the machine less protected.
- **Does not hold when**: The protection is triggered by a real mechanical jam.

## 6.2 Drum, heads, tape path and cleaning
- **Principle**: Dirt or residue on the drum lifts the tape from the heads and wrecks the picture.
- **How it works / sequence**: Clean heads and drum with isopropyl alcohol on a lint-free surface, always wiping along the direction of rotation per the manual; inspect the tape guides and rollers; clean connectors that carry sync signals.
- **Moves**:
  - Sticky residue near the base of the drum has been associated with tapes that shed binder.
  - Where tapes show mould, clean dry with a purpose-made tape cleaner (soft microfibre brush, passing in both directions) and check the brush afterwards.
  - Sticky-binder tapes are controversial; baking has been mentioned and is not recommended by the sources here without specialist guidance.
  - Check belts, loading belts and carriage belts, which are classic failures; a missing or fractured belt is common.
- **Evidence**: Practitioner; **Contested** on baking sticky tapes.
- **Trade-off**: Cleaning cycles cost tape wear; skipping cleaning risks head damage.
- **Does not hold when**: The drum bearing is noisy or the heads are worn; then replacement or specialist service.

## 6.3 Mechanics and sensors in older formats
- **Principle**: Older formats (professional cassettes, early home formats) have heavy mechanisms with many belts and tensioners.
- **How it works / sequence**: Check all belts first, then loading and carriage mechanisms; test the loading with an empty cassette shell before using real tape.
- **Moves**:
  - A loose set-screw (grub screw) on a gear can allow slip; a small dimple on the shaft can lock it.
  - Plastics may be brittle; handle gently.
  - A machine that fits a single mechanism swap from a donor may work after a transplant.
  - Before transferring tapes, set recording levels (a defined audio reference level) and confirm that video is on auto.
- **Evidence**: Practitioner
- **Trade-off**: Donor swaps preserve the machine and alter the original.
- **Does not hold when**: The mechanism is not available as spares.

## 6.4 Capture, time-base correction and transfer
- **Principle**: Analog video needs stable timing; a time-base corrector (TBC) re-times the signal so a capture card can lock onto it.
- **How it works / sequence**: Connect the recorder through its best output (S-video over composite where available) into a capture device that matches the standard (PAL or NTSC); use a TBC or a recorder with a built-in one when the capture drops; deinterlace to taste afterwards.
- **Moves**:
  - Without a TBC, unstable sync can make a capture freeze.
  - Connect ground; without it there may be no signal.
  - Some digital outputs on professional machines do not match the capture card; use the analog output.
  - Adaptive deinterlacing preserves detail in still areas and softens only in motion. **Position**.
  - A recorded S-video signal usually looks better than composite on the same tape, and "better than VHS" is true of S-video as a signal, not of the tape itself.
  - On a computer, some BIOS settings (such as large address windows) can prevent a capture card from working; disable them if the card fails to start.
- **Evidence**: Practitioner
- **Trade-off**: Hardware TBCs cost money and time; software correction exists and is less reliable.
- **Does not hold when**: The tape is damaged beyond what correction can handle.

## 6.5 Capture cards and period editing systems
- **Principle**: Old capture and editing cards were designed for a specific operating system, bus and drive combination.
- **How it works / sequence**: Use the era-appropriate OS and chipset; give the card its own storage; avoid resource conflicts with the disk controller.
- **Moves**:
  - These cards often work only on a specific OS version; later versions cannot install the drivers.
  - Clean card contacts and slots; verify the supply rails in the BIOS.
  - A card that conflicts with a SCSI controller may need a different slot or card arrangement.
  - Old cards sometimes need a PCI bus with enough bandwidth; a dedicated machine is common.
- **Evidence**: Practitioner
- **Trade-off**: A period machine is authentic but slow and demanding to keep alive.
- **Does not hold when**: A modern capture device does the job and you do not need the period workflow.

## 6.6 Cameras, lenses and film
- **Principle**: Camcorder and lens problems are mostly mechanical and optical, with sensors and filters ageing.
- **How it works / sequence**: Check focus behaviour with the viewfinder peaking aid, and set back-focus so the image stays sharp across zoom; clean and replace filters that have fogged.
- **Moves**:
  - A multi-layer infrared filter that has turned cloudy from moisture can be separated and cleaned in solvent; take care.
  - Closing the aperture reduces lens aberrations and raises sharpness when using a camcorder lens in a webcam setting, at the cost of light.
  - For small-gauge film, telecine is done by projecting onto a screen at 45 degrees and filming at the right frame rate with the correct shutter; film that is torn or glued needs specialist care.
  - A viewfinder with a squashed picture may have a failed capacitor in its small display circuit.
- **Evidence**: Practitioner
- **Trade-off**: Optical repairs risk breaking delicate parts.
- **Does not hold when**: The sensor or tube is worn out.

## 6.7 Television sets and CRT chassis
- **Principle**: A CRT set contains line and frame deflection, a flyback transformer, a high-voltage stage and often a chassis connected to the mains. It is the most hazardous consumer appliance in this skill.
- **How it works / sequence**: Understand the set from its manual; check mains safety; leave the high-voltage section to a qualified technician; for analysis, observe the symptom (no picture, no raster, narrow picture, no sound).
- **Moves**:
  - In monochrome sets and some colour sets, do not touch the chassis ground.
  - An isolation transformer is a minimum; the series lamp is not isolation.
  - Capacitors in the horizontal deflection filter are stressed and often need the higher-voltage version specified by the manual (chapter 4).
  - Deflection coil wiring can crack and make the beam move only in one direction.
  - Convergence, linearity, focus and colour adjustments belong with a trained technician.
  - Closed-down shops with old sets sometimes use a mirror to adjust a tube from behind; this is a workshop technique, not a home procedure.
- **Evidence**: Practitioner
- **Trade-off**: A repaired tube set is a historical object; the risk is real.
- **Does not hold when**: The display is a small low-voltage screen or a modern flat panel.

## 6.8 Adding inputs and modifying sets
- **Principle**: A composite input can be added to an old monochrome or colour set, at the cost of changing a safe design.
- **How it works / sequence**: Locate the video detector or sync separator in the schematic and inject at a defined point through a coupling capacitor and a matching resistor (typically 75 ohm termination); feed audio into the volume control stage; disable the tuner path if necessary.
- **Moves**:
  - Keep the modification reversible.
  - Modifying mains-connected circuits is a job for a competent person; the input signal must remain isolated from the mains-referenced chassis.
  - A monitor and a modulator in parallel on a single antenna output degrade the signal; use switches to select outputs.
- **Evidence**: Practitioner; Contested for exact injection points, which depend on the chassis.
- **Trade-off**: A modified set is usable with modern sources and loses originality.
- **Does not hold when**: The chassis is live and unisolated; then use a modulator instead.

## 6.9 Display technologies other than the simple tube
- **Principle**: Projection, reflective, electrostatic and transparent displays have their own faults.
- **How it works / sequence**: Check lamp, optics, mirrors, polarisers and drive electronics in turn.
- **Moves**:
  - Projection systems suffer from oxidised mirrors, dried grease and cracked lamps; choose LCD or DLP engines by the lamp and optics available.
  - Reflective displays need a polariser and a reflective layer to show an image.
  - Electrostatic (oscilloscope-type) tubes use high deflection voltages and must be treated as hazardous.
  - Backlight inverters in LCD monitors are high-voltage sources; a monitor with sparks inside should not be run.
- **Evidence**: Practitioner
- **Trade-off**: Exotic displays are rewarding and parts are hard to source.
- **Does not hold when**: The unit uses a plain, mass-produced panel.
