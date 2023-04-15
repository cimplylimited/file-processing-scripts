const fs = require('fs'); // Import the file system module
const path = require('path'); // Import the path module

const dirPath = '/Users/johndoe/Git/LexDAO/LexDAO_Membership_Token/Image_Files'; // Set the directory path
const nTimes = 5; // Set the number of times to copy each file

function doCopy(dirPath, nTimes) {
  if (!fs.existsSync(dirPath)) { // Check if the directory path exists
    throw new Error('Directory path does not exist'); // Throw an error if the directory path does not exist
  }

  process.chdir(path.join(process.cwd(), dirPath)); // Change the current working directory to the specified directory path

  for (const file of fs.readdirSync(process.cwd())) { // Loop through each file in the directory
    if (!fs.statSync(file).isFile() || file[0] === '.') { // Check if the file is a regular file and not a hidden file
      continue; // Skip the file if it's not a regular file or it's a hidden file
    }

    const { name, ext } = path.parse(file); // Get the filename and extension of the file

    console.log('This is the original file name:', name); // Log the original filename to the console

    const startInd = parseInt(name, 10); // Parse the filename as an integer

    for (let n = 1; n <= nTimes; n++) { // Loop nTimes times
      const newFile = path.join(process.cwd(), `${startInd + n}${ext}`); // Set the new filename
      fs.copyFileSync(path.join(process.cwd(), file), newFile); // Copy the file with the new filename
    }
  }
}

doCopy(dirPath, nTimes); // Call the doCopy function with the specified directory path and number of times to copy each file
