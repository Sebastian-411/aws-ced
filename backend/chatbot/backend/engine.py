from experta import *

general_recommendations_list = {
   1: """
   It is very likely that you have a Cooling Issue, remember:
   - Perform regular maintenance checks on the cooling system, including the radiator, hoses, and coolant levels.
   - Replace the coolant as per the manufacturer's recommended schedule to prevent corrosion and deposits.
   - Upgrade to high-performance coolant if driving in extreme conditions.
   - Keep the radiator clean and free from dirt or bugs to ensure optimal airflow.
   - Consider replacing older parts like the thermostat, water pump, or radiator if they show signs of aging.
   """,
   2: """
   It is very likely that you have a Transmission Issue, remember:
   - Schedule periodic transmission fluid changes to ensure smooth operation.
   - Use high-quality transmission fluid recommended by the vehicle manufacturer.
   - Avoid excessive towing or overloading to prevent unnecessary strain on the transmission.
   - Install a transmission cooler if the vehicle is used for heavy-duty tasks.
   - Plan for a professional transmission service every 30,000–50,000 miles or as recommended by the manufacturer.
   """,
   3: """
   It is very likely that you have a Steering Issue, remember:
   - Replace power steering fluid at regular intervals to avoid contamination.
   - Schedule regular alignments to reduce wear on steering components and tires.
   - Use high-quality lubricants for steering joints and linkages.
   - Periodically inspect and replace worn or damaged components like bushings, tie rods, and ball joints.
   - Invest in high-quality tires and maintain consistent tire pressure for better handling.
   """,
   4: """
   It is very likely that you have a Braking Issue, remember:
   - Replace brake pads and rotors as a preventive measure before they are completely worn.
   - Flush and replace brake fluid periodically to avoid moisture buildup and corrosion.
   - Inspect and replace brake lines and hoses if they show signs of wear or cracking.
   - Invest in high-performance braking systems if you frequently drive in demanding conditions.
   - Schedule regular brake inspections to identify potential issues early and avoid costly repairs.
   """
}

recommendations_list = {
    1: """
You have the symptom of: Engine Overheating    
    
1. Stop the vehicle: 
   - If you notice the temperature gauge in the red zone or see steam coming from the hood, pull over to a safe location immediately.

2. Turn off the engine: 
   - Allow the engine to cool down completely before opening the hood. This can take 15 to 30 minutes. Never open the radiator when the engine is hot.

3. Check coolant levels: 
   - Once the engine is cool, open the hood and inspect the coolant reservoir. If it's low or empty, this could be the cause of the overheating.

4. Add coolant or water: 
   - If you have coolant, add it. If not, use water as a temporary solution, but make sure to replace it with proper coolant as soon as possible.

5. Look for visible leaks: 
   - Check under the car for any leaking fluids. If you notice a leak, avoid driving too far until it's repaired.

6. Avoid using the air conditioning: 
   - If you must continue driving, turn off the air conditioning and set the heater to maximum. This helps reduce the engine's heat load.

7. Visit a mechanic: 
   - Even if you manage to cool the engine temporarily, it's crucial to have a mechanic inspect the cooling system (radiator, hoses, water pump, thermostat) to find the root cause.

8. Future prevention: 
   - Regularly check coolant levels and ensure the cooling system is maintained as recommended by the manufacturer.

Note: 
   - If you're not comfortable following these steps or don't have the necessary resources, call for roadside assistance to prevent further engine damage.
""",
2: """
You have the symptom of: Weak Air Conditioning

1. Check the air filter: 
   - A clogged cabin air filter can restrict airflow. Inspect it and replace it if it's dirty.

2. Verify the refrigerant levels: 
   - Low refrigerant levels are a common cause of weak air conditioning. Consider having a professional check and recharge the system.

3. Inspect the vents: 
   - Make sure the vents are not blocked by any objects and are fully open. 

4. Test the fan settings: 
   - Check if the fan is working properly at all speed settings. If not, the blower motor may need attention.

5. Look for unusual noises: 
   - Strange sounds when the AC is running may indicate issues with the compressor or other components.

6. Examine the condenser: 
   - The AC condenser, located near the front of the car, can get blocked by debris. Clean it if necessary.

7. Check for leaks: 
   - Refrigerant leaks can reduce cooling efficiency. Look for oily spots or seek professional help to inspect for leaks.

8. Avoid overloading the system: 
   - Don't expect the AC to cool effectively if the car has been sitting in extreme heat for long periods. Vent hot air by opening the windows before turning on the AC.

9. Visit a professional: 
   - If the issue persists, have a certified technician inspect the system for problems such as a failing compressor, faulty sensors, or electrical issues.

Note: 
   - Regular AC maintenance can help prevent weak performance and ensure optimal cooling.
""",
3: """
You have the symptom of: Fan Clutch Failure

1. Look for overheating: 
   - A failing fan clutch often causes the engine to overheat, especially in stop-and-go traffic or when idling.

2. Check fan noise: 
   - If the fan is making loud or unusual noises, it might indicate that the fan clutch is stuck or malfunctioning.

3. Inspect fan movement: 
   - With the engine off and cool, try to spin the fan by hand. A faulty clutch might make the fan spin too freely or feel overly stiff.

4. Observe fan speed: 
   - If the fan does not spin faster as the engine heats up, the fan clutch may not be engaging properly.

5. Look for physical damage: 
   - Inspect the fan and clutch for visible wear, cracks, or leaks, which can be signs of failure.

6. Test engine cooling: 
   - Run the engine and check if the fan starts spinning at higher speeds when the temperature increases. Lack of proper cooling could confirm the issue.

7. Avoid prolonged driving: 
   - Driving with a failing fan clutch can lead to engine overheating and severe damage. Minimize driving until the issue is resolved.

8. Visit a mechanic: 
   - A professional can confirm if the fan clutch is faulty and replace it if necessary. They can also check for related issues, such as thermostat or radiator problems.

Note: 
   - Regular maintenance of the cooling system can help detect fan clutch issues early and avoid engine overheating.
""",
4: """
You have the symptom of: Refrigerant Leak

1. Check for visible signs of leakage: 
   - Look for oily or greasy spots around the AC components, such as the hoses, connections, or compressor.

2. Inspect the refrigerant level: 
   - Low refrigerant levels often indicate a leak. Have a professional measure and refill the system if necessary.

3. Listen for hissing sounds: 
   - A refrigerant leak may produce a faint hissing noise, especially when the AC is running.

4. Monitor cooling performance: 
   - If the air conditioning is not cooling effectively or stops working altogether, a refrigerant leak might be the cause.

5. Test for moisture or frost: 
   - Leaks can cause unusual moisture or frost buildup near AC components due to escaping refrigerant.

6. Use a leak detection kit: 
   - If you are comfortable with DIY solutions, use a UV dye or electronic leak detector to locate the source of the leak.

7. Avoid using the AC: 
   - Running the AC with low refrigerant can damage the compressor and other components. Minimize use until the issue is fixed.

8. Visit a certified technician: 
   - A professional can locate and repair the leak, as well as recharge the system with the proper refrigerant.

9. Prevent future leaks: 
   - Regular AC maintenance and inspections can help catch small leaks before they become major issues.

Note: 
   - Handling refrigerants requires special equipment and certifications, so it’s best to rely on a professional for repairs.
""",
5:"""
You have the symptom of: Damaged Radiator Fins

1. Inspect the radiator fins: 
   - Check for bent, crushed, or clogged fins. This can restrict airflow and reduce cooling efficiency.

2. Clean the fins: 
   - Use a soft brush or compressed air to remove dirt, debris, or bugs lodged in the fins. Avoid using high-pressure water, as it can cause further damage.

3. Straighten bent fins: 
   - Carefully use a fin comb or a small flathead screwdriver to straighten any bent fins. Be gentle to avoid breaking them.

4. Check for corrosion: 
   - Inspect the radiator for signs of rust or corrosion around the fins, which may indicate a need for replacement.

5. Avoid physical damage: 
   - Be cautious during cleaning or maintenance to prevent bending or damaging the delicate fins.

6. Monitor engine temperature: 
   - If the radiator fins are severely damaged, the engine may overheat. Watch the temperature gauge closely when driving.

7. Test the cooling system: 
   - A professional can pressure-test the cooling system to ensure no further damage has occurred to the radiator or other components.

8. Replace the radiator if needed: 
   - If the fins are extensively damaged or the radiator is leaking, replacement may be necessary to restore proper cooling.

9. Prevent future damage: 
   - Avoid parking in areas with heavy debris, and install a radiator guard if frequent road debris is a concern.

Note: 
   - Regular inspection and maintenance of the radiator can help prevent overheating and prolong the life of the cooling system.
""",
6: """
You have the symptom of: Heater Core Issues

1. Check for weak or no heat: 
   - If the heater is blowing cool or lukewarm air, the heater core may be clogged or leaking.

2. Inspect for coolant leaks: 
   - Look under the dashboard or on the passenger-side floor for signs of coolant puddles, as a leaking heater core often causes this.

3. Monitor the windshield: 
   - Fogged-up windows or a sweet smell inside the car may indicate coolant vapor from a faulty heater core.

4. Check engine temperature: 
   - A failing heater core can cause engine overheating if coolant flow is restricted.

5. Inspect coolant levels: 
   - A leaking heater core may result in low coolant levels. Refill as necessary but address the root cause promptly.

6. Test the heater hoses: 
   - With the engine warm, feel the hoses leading to the heater core. One should be hot, and the other slightly cooler. If both are cool, the heater core may be blocked.

7. Flush the heater core: 
   - If blockage is suspected, a professional can perform a flush to remove debris and restore proper flow.

8. Avoid driving with a severe leak: 
   - A leaking heater core can quickly deplete coolant and lead to engine overheating. Minimize driving until it’s repaired.

9. Replace the heater core if needed: 
   - If the heater core is severely damaged or leaking, replacement is often the only solution.

10. Prevent future issues: 
   - Regular maintenance of the cooling system, including timely coolant replacement, can help keep the heater core in good condition.

Note: 
   - Heater core replacement can be complex and often requires professional assistance due to its location behind the dashboard.
""",
7: """
You have the symptom of: Coolant Smoke

1. Stop the vehicle immediately: 
   - If you notice white smoke coming from the engine bay or exhaust, pull over to a safe location and turn off the engine.

2. Check for overheating: 
   - Look at the temperature gauge on the dashboard. Coolant smoke is often associated with engine overheating.

3. Inspect for coolant leaks: 
   - Look under the vehicle for any puddles of coolant or inspect the radiator, hoses, and reservoir for signs of leakage.

4. Identify the source of the smoke: 
   - White smoke from the engine bay may indicate a leaking radiator or hose. White smoke from the exhaust could signal a more serious issue, like a blown head gasket.

5. Check coolant levels: 
   - After allowing the engine to cool completely, inspect the coolant reservoir. Low levels can confirm a leak or excessive consumption.

6. Avoid driving the vehicle: 
   - Continuing to drive with coolant smoke can lead to severe engine damage. Tow the car to a mechanic if necessary.

7. Look for other symptoms: 
   - Watch for signs like milky oil (which indicates coolant mixing with engine oil) or a sweet smell in the exhaust, which could point to a head gasket issue.

8. Visit a mechanic: 
   - A professional can pressure-test the cooling system to locate leaks or confirm if the head gasket is damaged.

9. Prevent future issues: 
   - Regularly inspect and maintain the cooling system. Replace worn hoses, refill coolant as needed, and monitor engine performance.

Note: 
   - Coolant smoke can indicate critical engine problems. Prompt attention is essential to avoid costly repairs.
""",
8: """
You have the symptom of: Engine Shutdown Due to Heat

1. Pull over immediately: 
   - If the engine shuts down due to heat, safely stop the vehicle to prevent further damage.

2. Let the engine cool: 
   - Wait at least 15–30 minutes before attempting to restart. Avoid opening the hood while the engine is hot.

3. Check coolant levels: 
   - After cooling, inspect the coolant reservoir. Low or empty levels could indicate a leak or overheating issue.

4. Inspect for leaks: 
   - Look under the vehicle for coolant puddles or other visible leaks.

5. Avoid driving long distances: 
   - Restart the engine only if necessary, and drive short distances while monitoring the temperature gauge.

6. Visit a mechanic: 
   - A professional can identify the root cause, such as a failing water pump, radiator issues, or thermostat problems.

7. Perform regular maintenance: 
   - Check coolant levels regularly and ensure timely servicing of the cooling system.
""",
9: """

You have the symptom of: High Cabin Air Temperature

1. Verify air conditioning operation: 
   - Ensure the AC system is functioning properly. Weak cooling could indicate low refrigerant or a clogged filter.

2. Check the cabin air filter: 
   - A dirty air filter can restrict airflow and raise cabin temperatures. Replace it if necessary.

3. Inspect AC vents: 
   - Make sure vents are not blocked and are fully open.

4. Monitor engine temperature: 
   - If the engine overheats, the cabin may also heat up. Address engine cooling issues first.

5. Look for AC compressor issues: 
   - A faulty compressor can cause poor cooling and high cabin temperatures.

6. Use sunshades: 
   - When parked in the sun, use sunshades or window covers to keep the cabin cooler.

7. Visit a professional: 
   - If the issue persists, have a mechanic inspect the AC system and cooling components.
""",

10: """
You have the symptom of: Irregular Gear Shifting

1. Check transmission fluid levels: 
   - Low or dirty transmission fluid can cause irregular shifting. Refill or replace as necessary.

2. Monitor for warning lights: 
   - Look for transmission-related warning lights on the dashboard.

3. Inspect the transmission system: 
   - Loose connections or worn components may cause irregular shifting.

4. Avoid aggressive driving: 
   - Hard accelerations and sudden stops can worsen transmission issues.

5. Update transmission software: 
   - Some issues may be resolved by updating the transmission control module (TCM) software.

6. Visit a mechanic: 
   - Have a professional inspect the transmission system for internal damage or sensor failures.
""",
11: """
You have the symptom of: Clutch Slipping

1. Check clutch pedal operation: 
   - Ensure the clutch pedal engages and disengages smoothly.

2. Monitor RPM behavior: 
   - High RPMs without a corresponding increase in speed often indicate clutch slipping.

3. Avoid overloading the vehicle: 
   - Excessive weight can put extra strain on the clutch.

4. Inspect for wear and tear: 
   - A worn-out clutch disc may need replacement.

5. Minimize clutch abuse: 
   - Avoid resting your foot on the clutch pedal and excessive clutch use in traffic.

6. Visit a mechanic: 
   - A professional can diagnose and replace the clutch if necessary.
""",

12: """
You have the symptom of: Engine Acceleration Problems

1. Verify throttle response: 
   - Check for delayed or unresponsive acceleration when pressing the gas pedal.

2. Inspect the air intake system: 
   - A clogged air filter or dirty throttle body can reduce engine performance.

3. Check fuel delivery: 
   - Low fuel pressure or a failing fuel pump can cause poor acceleration.

4. Monitor for warning lights: 
   - Engine warning lights may indicate issues with sensors or the fuel system.

5. Avoid heavy loads: 
   - Reduce the weight in the vehicle to improve acceleration performance temporarily.

6. Visit a mechanic: 
   - A professional can test the engine and diagnose acceleration issues.
""",
13: """
You have the symptom of: Harsh Shifting

1. Check transmission fluid: 
   - Low or degraded fluid can cause harsh shifting. Replace it if necessary.

2. Inspect transmission mounts: 
   - Worn or damaged mounts can result in harsh gear engagement.

3. Monitor shift timing: 
   - If shifts occur too early or late, the transmission control module may need recalibration.

4. Avoid aggressive driving: 
   - Smooth accelerations and braking can reduce shifting harshness.

5. Visit a mechanic: 
   - Have the transmission system inspected for internal damage or software updates.
""",
14: """
You have the symptom of: Grinding Transmission Noise
1. Check for worn gears: 
   - Grinding noises often indicate worn or damaged gears in the transmission.

2. Inspect transmission fluid: 
   - Low or contaminated fluid can lead to gear wear and grinding.

3. Avoid forceful shifting: 
   - For manual transmissions, ensure the clutch is fully engaged before shifting gears.

4. Look for bearing issues: 
   - Worn bearings can cause grinding sounds during operation.

5. Visit a mechanic: 
   - A professional can inspect and repair the transmission to address grinding noises.
""",
15: """
You have the symptom of: Poor Acceleration

1. Inspect air and fuel filters: 
   - Dirty filters can restrict airflow or fuel delivery, leading to poor acceleration.

2. Check spark plugs: 
   - Worn or fouled spark plugs can reduce engine efficiency and acceleration.

3. Monitor engine performance: 
   - Look for unusual vibrations or noises that may indicate engine trouble.

4. Inspect the exhaust system: 
   - A clogged catalytic converter or exhaust leak can reduce power output.

5. Avoid overloading: 
   - Reduce vehicle weight to improve acceleration temporarily.

6. Visit a mechanic: 
   - Have the engine and drivetrain inspected for issues affecting performance.
""",

16: """
You have the symptom of: Stuck Manual Gear Shift

    1. Check for clutch issues: 
       - A worn or faulty clutch can make manual gear shifting difficult or stuck.

    2. Inspect the shifter linkage: 
       - Misaligned or damaged linkage can prevent smooth gear engagement.

    3. Avoid forcing the gear: 
       - Forcing the shifter can cause further damage. Instead, release the clutch and try again.

    4. Inspect for debris: 
       - Dirt or debris near the shifter mechanism may cause it to get stuck.

    5. Visit a mechanic: 
       - A professional can diagnose and repair internal transmission or clutch problems.
    """,
    17: """
    You have the symptom of: Difficulty Engaging Gears
    
    1. Check transmission fluid levels: 
       - Low or dirty fluid can cause difficulty engaging gears. Refill or replace as necessary.

    2. Inspect the clutch: 
       - A worn clutch or air in the hydraulic system may prevent gear engagement.

    3. Test the gear shifter: 
       - Misaligned or damaged linkage could cause issues with shifting.

    4. Avoid aggressive use: 
       - Avoid forcing gears or driving aggressively, which can exacerbate the problem.

    5. Visit a mechanic: 
       - A professional inspection can identify and resolve underlying issues.
    """,
    18: """
    You have the symptom of: Transmission Fluid Leak
    
    1. Inspect for visible leaks: 
       - Look under the vehicle for red or brown fluid, indicating a transmission fluid leak.

    2. Check transmission fluid levels: 
       - Low fluid levels can confirm a leak. Refill only temporarily until the leak is repaired.

    3. Tighten loose components: 
       - Loose bolts or fittings near the transmission pan or cooler lines can cause leaks.

    4. Avoid driving with a leak: 
       - Driving with insufficient transmission fluid can cause severe damage.

    5. Visit a mechanic: 
       - A professional can locate and repair the source of the leak.
    """,
    19: """
    You have the symptom of: Delayed Transmission Response
    
    1. Check transmission fluid levels: 
       - Low or degraded fluid can cause delayed response when shifting gears.

    2. Inspect for electronic issues: 
       - Faulty sensors or the transmission control module may cause delays.

    3. Avoid aggressive driving: 
       - Smooth acceleration and braking can help mitigate the delay temporarily.

    4. Monitor for warning lights: 
       - Transmission-related warning lights may indicate an underlying issue.

    5. Visit a mechanic: 
       - A professional can inspect the system for mechanical or electronic problems.
    """,
    20: """
    You have the symptom of: Gears Not Engaging
    
    1. Check clutch operation: 
       - A worn or faulty clutch can prevent gears from engaging properly.

    2. Inspect the transmission system: 
       - Internal damage or misaligned components may cause this issue.

    3. Test the gear shifter: 
       - Stuck or damaged linkage could prevent gear engagement.

    4. Monitor for warning signs: 
       - Look for unusual noises or vibrations when attempting to engage gears.

    5. Visit a mechanic: 
       - A professional inspection is essential to resolve gear engagement issues.
    """,
    21: """
    You have the symptom of: Shifting Delay
    
    1. Check transmission fluid: 
       - Low or old fluid can cause delays when shifting gears.

    2. Inspect the transmission system: 
       - Worn components or internal damage may lead to shifting delays.

    3. Monitor driving habits: 
       - Avoid sudden accelerations or heavy loads, which can worsen the problem.

    4. Update software: 
       - A transmission control module (TCM) software update may resolve shifting delays.

    5. Visit a mechanic: 
       - A professional can diagnose and repair the issue effectively.
    """,
    22: """
    You have the symptom of: Transmission Overheating
    
    1. Check for overheating symptoms: 
       - High transmission fluid temperature can indicate an overheating transmission.

    2. Inspect the cooling system: 
       - A failing transmission cooler or radiator can lead to overheating.

    3. Monitor fluid levels: 
       - Low or degraded fluid can increase heat buildup in the transmission.

    4. Avoid heavy loads: 
       - Reduce vehicle weight and avoid towing until the issue is resolved.

    5. Visit a mechanic: 
       - A professional inspection can prevent further damage to the transmission.
    """,
    23: """
    You have the symptom of: Transmission Slipping During Acceleration
    
    1. Check transmission fluid: 
       - Low or degraded fluid can cause slipping during acceleration. Refill or replace if needed.

    2. Inspect for warning lights: 
       - Transmission-related lights may indicate internal problems.

    3. Avoid aggressive driving: 
       - Hard accelerations can worsen slipping issues.

    4. Visit a mechanic: 
       - A professional can inspect and repair the transmission system to prevent further damage.
    """,
    24: """
    You have the symptom of: Loss of Power When Shifting Gears
    
    1. Check clutch and transmission: 
       - A worn clutch or internal transmission issues can cause power loss when shifting gears.

    2. Monitor RPMs: 
       - A sudden increase in RPMs without acceleration may indicate slippage.

    3. Inspect for warning lights: 
       - Transmission or engine lights can provide clues about the issue.

    4. Avoid heavy loads: 
       - Driving with a lighter load can temporarily reduce strain on the drivetrain.

    5. Visit a mechanic: 
       - Have the drivetrain and transmission inspected for repair or adjustment.
    """,
    25: """
    You have the symptom of: Unusual Smell During Acceleration
    
    1. Check for fluid leaks: 
       - A burnt or unusual smell during acceleration may indicate leaking transmission or engine oil.

    2. Inspect for overheating: 
       - High temperatures can cause unusual smells from the engine bay or exhaust.

    3. Monitor performance: 
       - Check for additional symptoms like smoke, reduced power, or warning lights.

    4. Avoid prolonged driving: 
       - Continuing to drive can worsen the issue. Have the vehicle inspected promptly.

    5. Visit a mechanic: 
       - A professional can locate and resolve the source of the smell.
    """,
    
    26: """
    You have the symptom of: Stiff Steering Wheel
    
    1. Check power steering fluid levels: 
       - Low fluid can cause stiffness in the steering wheel.

    2. Inspect the power steering pump: 
       - A failing pump can make the steering wheel hard to turn.

    3. Look for belt issues: 
       - A worn or loose serpentine belt can affect steering performance.

    4. Inspect for steering rack issues: 
       - A damaged or worn steering rack can lead to stiffness.

    5. Visit a mechanic: 
       - A professional inspection can resolve the issue and prevent further damage.
    """,
    27: """
    You have the symptom of: Steering Wheel Vibration
    
    1. Check wheel alignment: 
       - Misaligned wheels can cause vibration in the steering wheel.

    2. Inspect tire balance: 
       - Unbalanced tires can lead to vibrations, especially at higher speeds.

    3. Look for suspension issues: 
       - Worn suspension components can contribute to vibrations while driving.

    4. Inspect the steering components: 
       - Damaged steering parts, such as the tie rods, may cause vibrations.

    5. Visit a mechanic: 
       - A professional can diagnose the root cause and recommend repairs.
    """,
    28: """
    You have the symptom of: Steering Wheel Pulling
    
    1. Check for misaligned wheels: 
       - Misalignment can cause the steering wheel to pull to one side.

    2. Inspect tire pressure: 
       - Uneven tire pressure can cause pulling during driving.

    3. Check suspension components: 
       - Worn suspension parts can contribute to steering issues.

    4. Look for brake problems: 
       - A sticking brake caliper can cause pulling while driving.

    5. Visit a mechanic: 
       - A mechanic can realign the wheels or fix the suspension system to prevent pulling.
    """,
    29: """
    You have the symptom of: Steering Column Noise
    
    1. Inspect the steering column: 
       - Worn or damaged components can cause noises while turning the steering wheel.

    2. Check for lubrication: 
       - Lack of lubrication in the steering column can lead to noise.

    3. Examine the steering rack: 
       - A malfunctioning steering rack may cause unusual noises.

    4. Look for worn bearings: 
       - Damaged bearings in the steering column can result in noise.

    5. Visit a mechanic: 
       - A professional can identify and fix the source of the noise in the steering system.
    """,
    30: """
    You have the symptom of: Excessive Steering Play
    
    1. Inspect steering components: 
       - Worn tie rods or a damaged steering rack can cause excessive play.

    2. Check for loose steering parts: 
       - Loose parts in the steering system can create excessive play.

    3. Look for worn suspension components: 
       - Worn suspension parts can affect steering responsiveness.

    4. Check the power steering system: 
       - Low fluid or a failing pump can lead to excess play in the steering wheel.

    5. Visit a mechanic: 
       - A professional can inspect and repair the steering components.
    """,
    31: """
    You have the symptom of: Heavy Steering Wheel
    
    1. Check the power steering fluid levels: 
       - Low fluid can make the steering wheel feel heavy and hard to turn.

    2. Inspect the power steering pump: 
       - A failing pump can cause the steering to become heavier.

    3. Look for belt issues: 
       - A loose or worn belt may cause difficulty in steering.

    4. Inspect for suspension problems: 
       - Worn suspension components can affect the ease of steering.

    5. Visit a mechanic: 
       - A professional can diagnose and resolve the issue with the steering system.
    """,
    32: """
    You have the symptom of: Misaligned Steering Wheel
    
    1. Check steering wheel alignment: 
       - Misaligned wheels or a damaged steering column can cause the wheel to be off-center.

    2. Inspect suspension components: 
       - Worn suspension parts may cause the steering wheel to appear misaligned.

    3. Look for issues with the steering rack: 
       - A malfunctioning steering rack can cause the wheel to be misaligned.

    4. Check for wear in the steering column: 
       - Worn parts in the column can also lead to misalignment.

    5. Visit a mechanic: 
       - A professional can properly align the steering system and correct misalignment.
    """,
    33: """
    You have the symptom of: Steering Fluid Leak
    
    1. Check for fluid leaks: 
       - Leaking steering fluid can lead to low levels, affecting the power steering system.

    2. Inspect steering hoses: 
       - Damaged or cracked hoses may cause fluid leakage.

    3. Look for leaks near the power steering pump: 
       - A failing pump can cause fluid to leak.

    4. Inspect the steering rack seals: 
       - Worn seals in the steering rack can lead to leaks.

    5. Visit a mechanic: 
       - A mechanic can find and fix leaks in the steering system.
    """,
    34: """
    You have the symptom of: Difficulty Turning the Steering Wheel
    
    1. Check power steering fluid levels: 
       - Low fluid can make the steering wheel difficult to turn.

    2. Inspect the power steering pump: 
       - A failing pump can make steering harder.

    3. Look for belt issues: 
       - A worn or loose serpentine belt can make turning harder.

    4. Check the steering rack: 
       - Problems with the steering rack can cause difficulty turning the wheel.

    5. Visit a mechanic: 
       - A professional can diagnose and repair the issue with the steering system.
    """,
    35: """
    You have the symptom of: Steering Wheel Vibration During Acceleration
    
    1. Check for unbalanced tires: 
       - Tires that are unbalanced can cause vibration during acceleration.

    2. Inspect suspension components: 
       - Worn suspension parts can contribute to steering wheel vibration.

    3. Examine the power steering system: 
       - Low fluid or a malfunctioning pump can cause vibration.

    4. Check alignment: 
       - Misalignment can contribute to steering wheel vibration.

    5. Visit a mechanic: 
       - A mechanic can perform a full inspection to identify the cause of the vibration.
    """,
    36: """
    You have the symptom of: Less Responsive Steering
    
    1. Inspect power steering fluid levels: 
       - Low fluid can make the steering feel less responsive.

    2. Check the steering pump: 
       - A failing pump can cause sluggish steering.

    3. Look for issues with the steering rack: 
       - A malfunctioning steering rack can contribute to less responsive steering.

    4. Inspect suspension components: 
       - Worn suspension parts can affect steering performance.

    5. Visit a mechanic: 
       - A professional can diagnose and resolve the steering responsiveness issue.
    """,
    37: """
    You have the symptom of: Squealing Noise When Turning
    
    1. Inspect the serpentine belt: 
       - A worn or damaged belt can cause squealing noises when turning.

    2. Check the power steering pump: 
       - A failing pump can cause squealing while turning.

    3. Examine the steering fluid: 
       - Low or dirty fluid can cause noises.

    4. Inspect steering column parts: 
       - Worn parts in the column may contribute to the noise.

    5. Visit a mechanic: 
       - A mechanic can address the squealing noise and prevent further damage.
    """,
    38: """
    You have the symptom of: Worn Brake Pads
    
    1. Check brake pad thickness: 
       - Worn brake pads will need to be replaced for proper braking.

    2. Inspect the brake rotors: 
       - Damaged rotors may cause uneven braking and further wear on the pads.

    3. Listen for squealing sounds: 
       - Squealing is often a sign of worn brake pads.

    4. Check for brake pad material wear: 
       - Brake pads with worn material should be replaced immediately.

    5. Visit a mechanic: 
       - A professional can replace the pads and ensure the braking system is functioning properly.
    """,
    39: """
    You have the symptom of: Stuck Brake Pedal
    
    1. Check for brake fluid leaks: 
       - Leaking fluid can cause reduced braking power and a stuck brake pedal.

    2. Inspect the brake master cylinder: 
       - A malfunctioning master cylinder may cause the brake pedal to get stuck.

    3. Look for issues with the brake booster: 
       - A failing booster can cause abnormal pedal behavior.

    4. Examine the brake lines: 
       - Clogged or blocked brake lines can lead to the pedal getting stuck.

    5. Visit a mechanic: 
       - A professional can identify and repair the cause of the stuck brake pedal.
    """,
    40: """
    You have the symptom of: Flashing Brake Light
    
    1. Check the brake light switch: 
       - A malfunctioning switch may cause the brake light to flash unexpectedly.

    2. Inspect brake pads and discs: 
       - Excessive wear may cause irregular brake light flashing.

    3. Examine the brake fluid: 
       - Low fluid levels can cause the brake light to turn on.

    4. Check for electrical issues: 
       - Wiring problems may trigger the flashing light.

    5. Visit a mechanic: 
       - A professional can diagnose the issue with the brake system or electrical wiring.
    """,
    41: """
    You have the symptom of: Lack of Brake Response
    
    1. Check brake fluid levels: 
       - Low brake fluid can cause a lack of brake response.

    2. Inspect brake lines for leaks: 
       - Leaking brake lines can result in a loss of braking power.

    3. Examine the brake master cylinder: 
       - A failing master cylinder can affect brake response.

    4. Check for worn brake components: 
       - Worn brake pads or rotors can cause poor braking response.

    5. Visit a mechanic: 
       - A professional can check and repair the brake system for proper functionality.
    """,
    42: """
    You have the symptom of: Vibration When Stopping
    
    1. Check brake pads and rotors: 
       - Worn brake pads or warped rotors can cause vibrations when stopping.

    2. Inspect suspension components: 
       - Worn suspension parts can contribute to vibrations when braking.

    3. Examine the brake fluid: 
       - Low or contaminated brake fluid can affect braking performance.

    4. Check for warped brake discs: 
       - Warped discs can cause vibrations when applying the brakes.

    5. Visit a mechanic: 
       - A professional can identify and address the cause of the vibration when stopping.
    """,
    43: """
    You have the symptom of: Soft Brake Pedal
    
    1. Inspect the brake fluid: 
       - Low or contaminated fluid can cause the brake pedal to feel soft.

    2. Check for air in the brake lines: 
       - Air in the lines can reduce braking effectiveness and cause a soft pedal.

    3. Inspect brake pads and rotors: 
       - Worn pads and rotors may cause the brake pedal to feel softer than usual.

    4. Examine the brake master cylinder: 
       - A malfunctioning master cylinder can lead to a soft pedal.

    5. Visit a mechanic: 
       - A mechanic can check the brake system and restore proper braking performance.
    """,
    44: """
    You have the symptom of: Contaminated Brake Fluid
    
    1. Check brake fluid: 
       - Contaminated brake fluid can reduce braking efficiency and may damage brake components.

    2. Inspect the brake lines: 
       - Leaking or damaged lines can lead to contamination of the brake fluid.

    3. Examine the brake master cylinder: 
       - A failing master cylinder can introduce contaminants into the brake fluid.

    4. Change the brake fluid: 
       - Flush and replace the contaminated fluid to ensure the system functions properly.

    5. Visit a mechanic: 
       - A mechanic can flush the brake fluid and ensure the brake system is clean and efficient.
    """,
    45: """
    You have the symptom of: ABS Light On
    
    1. Check for ABS system faults: 
       - A malfunctioning ABS system can cause the ABS light to turn on.

    2. Inspect wheel speed sensors: 
       - Faulty wheel sensors can trigger the ABS light.

    3. Examine the brake system for issues: 
       - Problems with the brake components may cause the ABS light to activate.

    4. Inspect the ABS module: 
       - A failing ABS module can turn on the ABS warning light.

    5. Visit a mechanic: 
       - A professional can diagnose the ABS issue and reset the warning light.
    """,
    46: """
    You have the symptom of: Brake Fading With Heavy Use
    
    1. Check the brake fluid levels: 
       - Low fluid can cause fading during heavy braking.

    2. Inspect brake pads and rotors: 
       - Worn pads or warped rotors can cause fading under heavy use.

    3. Check for brake overheating: 
       - Overheating of the brake system may result in fading.

    4. Examine the brake master cylinder: 
       - A failing master cylinder can contribute to brake fading.

    5. Visit a mechanic: 
       - A professional can inspect and repair the brake system to prevent fading during use.
    """,
    47: """
    You have the symptom of: Squealing Brakes When Cold
    
    1. Inspect brake pads: 
       - Cold weather can cause the brake pads to squeal if they are worn or contaminated.

    2. Check brake rotors: 
       - Warped or dirty rotors can also contribute to squealing noises when the brakes are cold.

    3. Examine brake fluid levels: 
       - Low fluid can affect brake performance, especially in colder temperatures.

    4. Check for moisture on the brake pads: 
       - Moisture or ice buildup on the pads can cause squealing during cold weather.

    5. Visit a mechanic: 
       - A professional can inspect and clean the brake system to reduce squealing noises.
    """,
    48: """
    You have the symptom of: Grinding Feel When Braking
    
    1. Inspect brake pads and rotors: 
       - Worn or damaged brake pads can cause a grinding sensation when braking.

    2. Check for debris between pads and rotors: 
       - Foreign objects or dirt can cause a grinding feel when applying the brakes.

    3. Examine the brake calipers: 
       - Sticky or malfunctioning calipers can lead to uneven braking and grinding.

    4. Check the brake fluid: 
       - Low or contaminated brake fluid can affect braking performance and lead to grinding.

    5. Visit a mechanic: 
       - A professional can replace the brake pads or rotors if they are damaged and resolve the grinding issue.
    """,
    49: """
    You have the symptom of: Failure to Stop Quickly
    
    1. Inspect brake pads and rotors: 
       - Worn pads or warped rotors can affect the ability to stop quickly.

    2. Examine the brake master cylinder: 
       - A failing master cylinder can cause delayed braking response.

    3. Check for brake fluid leaks: 
       - A fluid leak can result in insufficient braking power and failure to stop quickly.

    4. Inspect the brake lines: 
       - Leaks in the brake lines can cause a reduction in braking performance.

    5. Visit a mechanic: 
       - A professional can inspect the braking system and replace worn or damaged components to restore full braking power.
    """,
    50: """
    You have the symptom of: Brake Line Leak
    
    1. Check brake lines for leaks: 
       - Leaking brake lines can cause a loss of brake fluid and reduce braking effectiveness.

    2. Inspect the brake calipers: 
       - Malfunctioning calipers can cause fluid leakage and affect brake function.

    3. Examine the brake fluid reservoir: 
       - A low brake fluid level due to leaks can cause inadequate braking.

    4. Inspect the brake fittings: 
       - Loose or damaged fittings can cause brake fluid to leak from the system.

    5. Visit a mechanic: 
       - A mechanic can locate the leak and repair or replace the damaged parts to restore brake performance.
    """,
    51: """
    You have the symptom of: Whistling Noise When Pressing the Brake
    
    1. Check the brake pads and rotors: 
       - Worn or uneven brake pads can cause a whistling noise when pressing the brake pedal.

    2. Inspect brake fluid: 
       - Contaminated or low fluid levels can cause irregular brake performance, contributing to whistling.

    3. Examine the brake system for air pockets: 
       - Air in the brake lines can affect performance and produce unusual sounds.

    4. Inspect the brake hoses: 
       - Worn or damaged hoses can cause a whistling noise due to air or fluid flow issues.

    5. Visit a mechanic: 
       - A professional can inspect the braking system and fix any issues that are causing the whistling sound.
    """,
    52: """
    You have the symptom of: Excessive Brake Pedal Travel
    
    1. Check the brake fluid level: 
       - Low brake fluid can cause excessive brake pedal travel.

    2. Inspect the brake master cylinder: 
       - A faulty master cylinder can contribute to excessive pedal travel.

    3. Examine the brake lines for air: 
       - Air in the brake lines can lead to longer pedal travel and reduced braking effectiveness.

    4. Check brake pads and rotors: 
       - Worn components may require the brake pedal to be pushed further to achieve stopping power.

    5. Visit a mechanic: 
       - A mechanic can inspect and replace any worn or damaged components to reduce pedal travel.
    """,
    53: """
    You have the symptom of: Hard Brake Pedal
    
    1. Inspect the brake booster: 
       - A faulty brake booster can cause the brake pedal to feel harder than usual.

    2. Check the vacuum lines: 
       - Leaks or blockages in the vacuum lines can reduce the effectiveness of the brake booster.

    3. Examine the master cylinder: 
       - A failing master cylinder can cause the pedal to feel abnormally hard.

    4. Inspect brake fluid: 
       - Low fluid levels can affect the brake pedal's pressure, making it feel hard.

    5. Visit a mechanic: 
       - A professional can inspect and repair the brake booster and related components.
    """,
    54: """
    You have the symptom of: ABS Failure
    
    1. Inspect the ABS module: 
       - A malfunctioning ABS module can cause the ABS system to fail.

    2. Check the ABS wheel speed sensors: 
       - Faulty sensors can prevent the ABS from functioning correctly.

    3. Examine the ABS pump and valves: 
       - Damaged or malfunctioning parts can cause the ABS failure.

    4. Inspect the fuse for the ABS system: 
       - A blown fuse can prevent the ABS from engaging.

    5. Visit a mechanic: 
       - A mechanic can diagnose and repair the ABS system to restore full functionality.
    """
}


class Symptom(Fact):
    pass

class Engine(KnowledgeEngine):
    def __init__(self):
        super().__init__()

        self.recommendations = {}
    
    
    # Cooling Issue
    @Rule(Fact(fact='Cooling_Issue'))
    def cooling_issue_flow(self):
        self.recommendations["Cooling_Issue"] = general_recommendations_list[1]
    
    # Transmission Issue
    @Rule(Fact(fact='Transmission_Issue'))
    def transmission_issue_flow(self):
        self.recommendations["Transmission_Issue"] = general_recommendations_list[2]

    # Steering Issue
    @Rule(Fact(fact='Steering_Issue'))
    def steering_issue_flow(self):
        self.recommendations["Steering_Issue"] = general_recommendations_list[3]

    # Braking Issue
    @Rule(Fact(fact='Braking_Issue'))
    def braking_issue_flow(self):
        self.recommendations["Braking_Issue"] = general_recommendations_list[4]


    # For individual symptoms
    
    #1
    @Rule(Symptom(name="Symptom_Engine_Overheating"))
    def symptom_engine_overheating(self):
        self.recommendations["Symptom_Engine_Overheating"] = recommendations_list[1]
    #2
    @Rule(Symptom(name="Symptom_Weak_Air_Conditioning"))
    def symptom_weak_air_conditioning(self):
        self.recommendations["Symptom_Weak_Air_Conditioning"] = recommendations_list[2]
    #3
    @Rule(Symptom(name="Symptom_Fan_Clutch_Failure"))
    def symptom_fan_clutch_failure(self):
        self.recommendations["Symptom_Fan_Clutch_Failure"] = recommendations_list[3]
    #4
    @Rule(Symptom(name="Symptom_Refrigerant_Leak"))
    def symptom_refrigerant_leak(self):
        self.recommendations["Symptom_Refrigerant_Leak"] = recommendations_list[4]
    #5
    @Rule(Symptom(name="Symptom_Damaged_Radiator_Fins"))
    def symptom_damaged_radiator_fins(self):
        self.recommendations["Symptom_Damaged_Radiator_Fins"] = recommendations_list[5]
    #6
    @Rule(Symptom(name="Symptom_Heater_Core_Issues"))
    def symptom_heater_core_issues(self):
        self.recommendations["Symptom_Heater_Core_Issues"] = recommendations_list[6]
    #7
    @Rule(Symptom(name="Symptom_Coolant_Smoke"))
    def symptom_coolant_smoke(self):
        self.recommendations["Symptom_Coolant_Smoke"] = recommendations_list[7]
    #8
    @Rule(Symptom(name="Symptom_Engine_Shutdown_Heat"))
    def symptom_engine_shutdown_heat(self):
        self.recommendations["Symptom_Engine_Shutdown_Heat"] = recommendations_list[8]
    #9
    @Rule(Symptom(name="Symptom_High_Cabin_Air_Temperature"))
    def symptom_high_cabin_air_temperature(self):
        self.recommendations["Symptom_High_Cabin_Air_Temperature"] = recommendations_list[9]
    #10
    @Rule(Symptom(name="Symptom_Irregular_Gear_Shifting"))
    def symptom_irregular_gear_shifting(self):
        self.recommendations["Symptom_Irregular_Gear_Shifting"] = recommendations_list[10]
    #11
    @Rule(Symptom(name="Symptom_Clutch_Slipping"))
    def symptom_clutch_slipping(self):
        self.recommendations["Symptom_Clutch_Slipping"] = recommendations_list[11]
    #12
    @Rule(Symptom(name="Symptom_Engine_Acceleration"))
    def symptom_engine_acceleration(self):
        self.recommendations["Symptom_Engine_Acceleration"] = recommendations_list[12]
    #13
    @Rule(Symptom(name="Symptom_Harsh_Shifting"))
    def symptom_harsh_shifting(self):
        self.recommendations["Symptom_Harsh_Shifting"] = recommendations_list[13]
    #14
    @Rule(Symptom(name="Symptom_Grinding_Transmission_Noise"))
    def symptom_grinding_transmission_noise(self):
        self.recommendations["Symptom_Grinding_Transmission_Noise"] = recommendations_list[14]
    #15
    @Rule(Symptom(name="Symptom_Poor_Acceleration"))
    def symptom_poor_acceleration(self):
        self.recommendations["Symptom_Poor_Acceleration"] = recommendations_list[15]
    #16
    @Rule(Symptom(name="Symptom_Stuck_Manual_Gear_Shift"))
    def symptom_stuck_manual_gear_shift(self):
        self.recommendations["Symptom_Stuck_Manual_Gear_Shift"] = recommendations_list[16]
    #17
    @Rule(Symptom(name="Symptom_Difficulty_Engaging_Gears"))
    def symptom_difficulty_engaging_gears(self):
        self.recommendations["Symptom_Difficulty_Engaging_Gears"] = recommendations_list[17]
    #18
    @Rule(Symptom(name="Symptom_Transmission_Fluid_Leak"))
    def symptom_transmission_fluid_leak(self):
        self.recommendations["Symptom_Transmission_Fluid_Leak"] = recommendations_list[18]
    #19
    @Rule(Symptom(name="Symptom_Delayed_Transmission_Response"))
    def symptom_delayed_transmission_response(self):
        self.recommendations["Symptom_Delayed_Transmission_Response"] = recommendations_list[19]
    #20
    @Rule(Symptom(name="Symptom_Gears_Not_Engaging"))
    def symptom_gears_not_engaging(self):
        self.recommendations["Symptom_Gears_Not_Engaging"] = recommendations_list[20]
    #21
    @Rule(Symptom(name="Symptom_Shifting_Delay"))
    def symptom_shifting_delay(self):
        self.recommendations["Symptom_Shifting_Delay"] = recommendations_list[21]
    #22
    @Rule(Symptom(name="Symptom_Transmission_Overheating"))
    def symptom_transmission_overheating(self):
        self.recommendations["Symptom_Transmission_Overheating"] = recommendations_list[22]
    #23
    @Rule(Symptom(name="Symptom_Transmission_Slipping_Acceleration"))
    def symptom_transmission_slipping_acceleration(self):
        self.recommendations["Symptom_Transmission_Slipping_Acceleration"] = recommendations_list[23]
    #24
    @Rule(Symptom(name="Symptom_Loss_of_Power_Gear_Shifting"))
    def symptom_loss_of_power_gear_shifting(self):
        self.recommendations["Symptom_Loss_of_Power_Gear_Shifting"] = recommendations_list[24]
    #25
    @Rule(Symptom(name="Symptom_Unusual_Smell_Acceleration"))
    def symptom_unusual_smell_acceleration(self):
        self.recommendations["Symptom_Unusual_Smell_Acceleration"] = recommendations_list[25]
    #26
    @Rule(Symptom(name="Symptom_Stiff_Steering_Wheel"))
    def symptom_stiff_steering_wheel(self):
        self.recommendations["Symptom_Stiff_Steering_Wheel"] = recommendations_list[26]
    #27
    @Rule(Symptom(name="Symptom_Steering_Wheel_Vibration"))
    def symptom_steering_wheel_vibration(self):
        self.recommendations["Symptom_Steering_Wheel_Vibration"] = recommendations_list[27]
    #28
    @Rule(Symptom(name="Symptom_Steering_Wheel_Pulling"))
    def symptom_steering_wheel_pulling(self):
        self.recommendations["Symptom_Steering_Wheel_Pulling"] = recommendations_list[28]
    #29
    @Rule(Symptom(name="Symptom_Steering_Column_Noise"))
    def symptom_steering_column_noise(self):
        self.recommendations["Symptom_Steering_Column_Noise"] = recommendations_list[29]
    #30
    @Rule(Symptom(name="Symptom_Excessive_Steering_Play"))
    def symptom_excessive_steering_play(self):
        self.recommendations["Symptom_Excessive_Steering_Play"] = recommendations_list[30]
    #31
    @Rule(Symptom(name="Symptom_Heavy_Steering_Wheel"))
    def symptom_heavy_steering_wheel(self):
        self.recommendations["Symptom_Heavy_Steering_Wheel"] = recommendations_list[31]
    #32
    @Rule(Symptom(name="Symptom_Misaligned_Steering_Wheel"))
    def symptom_misaligned_steering_wheel(self):
        self.recommendations["Symptom_Misaligned_Steering_Wheel"] = recommendations_list[32]
    #33
    @Rule(Symptom(name="Symptom_Steering_Fluid_Leak"))
    def symptom_steering_fluid_leak(self):
        self.recommendations["Symptom_Steering_Fluid_Leak"] = recommendations_list[33]
    #34
    @Rule(Symptom(name="Symptom_Difficulty_Turning_Steering_Wheel"))
    def symptom_difficulty_turning_steering_wheel(self):
        self.recommendations["Symptom_Difficulty_Turning_Steering_Wheel"] = recommendations_list[34]
    #35
    @Rule(Symptom(name="Symptom_Steering_Wheel_Vibration_Acceleration"))
    def symptom_steering_wheel_vibration_acceleration(self):
        self.recommendations["Symptom_Steering_Wheel_Vibration_Acceleration"] = recommendations_list[35]
    #36
    @Rule(Symptom(name="Symptom_Less_Responsive_Steering"))
    def symptom_less_responsive_steering(self):
        self.recommendations["Symptom_Less_Responsive_Steering"] = recommendations_list[36]
    #37
    @Rule(Symptom(name="Symptom_Squealing_Noise_Turning"))
    def symptom_squealing_noise_turning(self):
        self.recommendations["Symptom_Squealing_Noise_Turning"] = recommendations_list[37]
    #38
    @Rule(Symptom(name="Symptom_Worn_Brake_Pads"))
    def symptom_worn_brake_pads(self):
        self.recommendations["Symptom_Worn_Brake_Pads"] = recommendations_list[38]
    #39
    @Rule(Symptom(name="Symptom_Stuck_Brake_Pedal"))
    def symptom_stuck_brake_pedal(self):
        self.recommendations["Symptom_Stuck_Brake_Pedal"] = recommendations_list[39]
    #40
    @Rule(Symptom(name="Symptom_Flashing_Brake_Light"))
    def symptom_flashing_brake_light(self):
        self.recommendations["Symptom_Flashing_Brake_Light"] = recommendations_list[40]
    #41
    @Rule(Symptom(name="Symptom_Lack_of_Brake_Response"))
    def symptom_lack_of_brake_response(self):
        self.recommendations["Symptom_Lack_of_Brake_Response"] = recommendations_list[41]
    #42
    @Rule(Symptom(name="Symptom_Vibration_When_Stopping"))
    def symptom_vibration_when_stopping(self):
        self.recommendations["Symptom_Vibration_When_Stopping"] = recommendations_list[42]
    #43
    @Rule(Symptom(name="Symptom_Soft_Brake_Pedal"))
    def symptom_soft_brake_pedal(self):
        self.recommendations["Symptom_Soft_Brake_Pedal"] = recommendations_list[43]
    #44
    @Rule(Symptom(name="Symptom_Contaminated_Brake_Fluid"))
    def symptom_contaminated_brake_fluid(self):
        self.recommendations["Symptom_Contaminated_Brake_Fluid"] = recommendations_list[44]
    #45
    @Rule(Symptom(name="Symptom_ABS_Light_On"))
    def symptom_abs_light_on(self):
        self.recommendations["Symptom_ABS_Light_On"] = recommendations_list[45]
    #46
    @Rule(Symptom(name="Symptom_Brake_Fading_With_Heavy_Use"))
    def symptom_brake_fading_with_heavy_use(self):
        self.recommendations["Symptom_Brake_Fading_With_Heavy_Use"] = recommendations_list[46]

    #47
    @Rule(Symptom(name="Symptom_Squealing_Brakes_When_Cold"))
    def symptom_squealing_brakes_when_cold(self):
        self.recommendations["Symptom_Squealing_Brakes_When_Cold"] = recommendations_list[47]

    #48
    @Rule(Symptom(name="Symptom_Grinding_Feel_Brakes"))
    def symptom_grinding_feel_brakes(self):
        self.recommendations["Symptom_Grinding_Feel_Brakes"] = recommendations_list[48]

    #49
    @Rule(Symptom(name="Symptom_Failure_to_Stop_Quickly"))
    def symptom_failure_to_stop_quickly(self):
        self.recommendations["Symptom_Failure_to_Stop_Quickly"] = recommendations_list[49]

    #50
    @Rule(Symptom(name="Symptom_Brake_Line_Leak"))
    def symptom_brake_line_leak(self):
        self.recommendations["Symptom_Brake_Line_Leak"] = recommendations_list[50]

    #51
    @Rule(Symptom(name="Symptom_Whistling_Noise_When_Pressing_Brake"))
    def symptom_whistling_noise_when_pressing_brake(self):
        self.recommendations["Symptom_Whistling_Noise_When_Pressing_Brake"] = recommendations_list[51]

    #52
    @Rule(Symptom(name="Symptom_Excessive_Brake_Pedal_Travel"))
    def symptom_excessive_brake_pedal_travel(self):
        self.recommendations["Symptom_Excessive_Brake_Pedal_Travel"] = recommendations_list[52]

    #53
    @Rule(Symptom(name="Symptom_Hard_Brake_Pedal"))
    def symptom_hard_brake_pedal(self):
        self.recommendations["Symptom_Hard_Brake_Pedal"] = recommendations_list[53]

    #54
    @Rule(Symptom(name="Symptom_ABS_Failure"))
    def symptom_abs_failure(self):
        self.recommendations["Symptom_ABS_Failure"] = recommendations_list[54]
        
    def reset_recommendations(self):
        self.recommendations.clear()

class GeneralEngine():
   
   def make_recommendations(self,bayesian_diagnostic):
      engine = Engine()
      
      engine.reset_recommendations()

      engine.reset()
         
      for fact in bayesian_diagnostic.get("facts", []):
            engine.declare(Fact(fact=fact))

      for symptom in bayesian_diagnostic.get("symptoms", []):
            engine.declare(Symptom(name=symptom))
         
      engine.run()
         
      bayesian_diagnostic["recommendations"] = engine.recommendations
         
      return bayesian_diagnostic