export interface Question {
  id: number;
  text: string;
  category: string;
}

export const diagnosticQuestions: Question[] = [
  { id: 1, text: "Have you noticed the engine temperature exceeding normal levels?", category: "Cooling System Issues" },
  { id: 2, text: "Is the air conditioning in your vehicle cooling less than usual?", category: "Cooling System Issues" },
  { id: 3, text: "Does the engine fan not operate consistently or properly?", category: "Cooling System Issues" },
  { id: 4, text: "Have you observed fluid spots under the vehicle?", category: "Cooling System Issues" },
  { id: 5, text: "Have you noticed visible damage to the radiator fins?", category: "Cooling System Issues" },
  { id: 6, text: "Does the vehicle's heating system not heat as it should?", category: "Cooling System Issues" },
  { id: 7, text: "Have you seen smoke coming from the hood or cooling system?", category: "Cooling System Issues" },
  { id: 8, text: "Does the engine shut off after prolonged use or under high temperatures?", category: "Cooling System Issues" },
  { id: 9, text: "Is the air inside the cabin hotter than normal?", category: "Cooling System Issues" },
  { id: 10, text: "Have you noticed irregularities when shifting gears?", category: "Transmission Issues" },
  { id: 11, text: "Does the engine rev up, but the vehicle speed doesn't increase proportionally?", category: "Transmission Issues" },
  { id: 12, text: "Does the engine accelerate unexpectedly without any apparent reason?", category: "Transmission Issues" },
  { id: 13, text: "Are the gear shifts abrupt or sudden?", category: "Transmission Issues" },
  { id: 14, text: "Do you hear a grinding noise while operating the transmission?", category: "Transmission Issues" },
  { id: 15, text: "Does the vehicle take longer than usual to respond when accelerating?", category: "Transmission Issues" },
  { id: 16, text: "Have you experienced difficulty moving the gear shift?", category: "Transmission Issues" },
  { id: 17, text: "Is it hard to shift into the desired gear?", category: "Transmission Issues" },
  { id: 18, text: "Have you noticed reddish or oily spots under the vehicle?", category: "Transmission Issues" },
  { id: 19, text: "Does the transmission take longer than usual to respond?", category: "Transmission Issues" },
  { id: 20, text: "Have you noticed that certain gears won't engage when you try to use them?", category: "Transmission Issues" },
  { id: 21, text: "Is there a noticeable delay when shifting gears?", category: "Transmission Issues" },
  { id: 22, text: "Is the transmission hotter than usual?", category: "Transmission Issues" },
  { id: 23, text: "Does the vehicle fail to accelerate properly when you speed up?", category: "Transmission Issues" },
  { id: 24, text: "Does the vehicle lose power when changing gears?", category: "Transmission Issues" },
  { id: 25, text: "Do you notice a strange smell when accelerating?", category: "Transmission Issues" },
  { id: 26, text: "Do you find it difficult to turn the steering wheel?", category: "Steering Issues" },
  { id: 27, text: "Does the steering wheel vibrate while driving?", category: "Steering Issues" },
  { id: 28, text: "Does the steering wheel tend to pull to one side while driving?", category: "Steering Issues" },
  { id: 29, text: "Do you hear any noise coming from the steering column?", category: "Steering Issues" },
  { id: 30, text: "Does the steering wheel move excessively without affecting the vehicle's direction?", category: "Steering Issues" },
  { id: 31, text: "Does the steering wheel feel heavier than usual when turning?", category: "Steering Issues" },
  { id: 32, text: "Is the steering wheel misaligned when driving straight?", category: "Steering Issues" },
  { id: 33, text: "Have you noticed any steering fluid leakage?", category: "Steering Issues" },
  { id: 34, text: "Is it hard to turn the steering wheel in any direction?", category: "Steering Issues" },
  { id: 35, text: "Does the steering wheel vibrate more when accelerating?", category: "Steering Issues" },
  { id: 36, text: "Does the vehicle not respond quickly to steering wheel movements?", category: "Steering Issues" },
  { id: 37, text: "Do you hear a squealing sound when turning the steering wheel?", category: "Steering Issues" },
  { id: 38, text: "Do the brakes make a metallic sound when used?", category: "Brake Issues" },
  { id: 39, text: "Does the brake pedal not return easily after pressing it?", category: "Brake Issues" },
  { id: 40, text: "Is the brake light on the dashboard flashing or staying on?", category: "Brake Issues" },
  { id: 41, text: "Do the brakes take longer to stop the vehicle than usual?", category: "Brake Issues" },
  { id: 42, text: "Do you feel vibrations in the vehicle when braking?", category: "Brake Issues" },
  { id: 43, text: "Does the brake pedal feel softer than normal?", category: "Brake Issues" },
  { id: 44, text: "Does the brake fluid appear dark or dirty?", category: "Brake Issues" },
  { id: 45, text: "Is the ABS light illuminated on the dashboard?", category: "Brake Issues" },
  { id: 46, text: "Do the brakes lose effectiveness after extended use?", category: "Brake Issues" },
  { id: 47, text: "Do the brakes squeal when used in cold conditions?", category: "Brake Issues" },
  { id: 48, text: "Do the brakes feel rough or grinding?", category: "Brake Issues" },
  { id: 49, text: "Does the vehicle fail to stop quickly during an emergency braking situation?", category: "Brake Issues" },
  { id: 50, text: "Have you noticed any leakage in the brake lines?", category: "Brake Issues" },
  { id: 51, text: "Do you hear a whistling noise when pressing the brake pedal?", category: "Brake Issues" },
  { id: 52, text: "Does the brake pedal need to be pressed further than usual to stop the vehicle?", category: "Brake Issues" },
  { id: 53, text: "Does the brake pedal feel unusually stiff?", category: "Brake Issues" },
  { id: 54, text: "Does the ABS system fail to operate as expected when braking?", category: "Brake Issues" }
];