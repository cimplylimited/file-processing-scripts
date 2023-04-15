const fs = require('fs'); // Import the file system module
const path = require('path'); // Import the path module

const dirPath = '/Users/johndoe/Git/LexDAO/LexDAO_Membership_Token/Token_Files'; // Set the directory path
const nTimes = 200; // Set the number of times to copy each file
const fileName = '0.json'; // Set the filename to start with (currently not used)

const newFilesList = []; // Initialize an array to hold the paths of the new files

function fileIncrement(dirPath, nTimes) {
  if (!fs.existsSync(dirPath)) { // Check if the directory path exists
    throw new Error('Directory path does not exist'); // Throw an error if the directory path does not exist
  }

  process.chdir(dirPath); // Change the current working directory to the specified directory path

  for (const file of fs.readdirSync(process.cwd())) { // Loop through each file in the directory
    if (!fs.statSync(file).isFile() || file[0] === '.') { // Check if the file is a regular file and not a hidden file
      continue; // Skip the file if it's not a regular file or it's a hidden file
    }

    const { name, ext } = path.parse(file); // Get the filename and extension of the file

    const startInd = parseInt(name, 10); // Parse the filename as an integer

    for (let n = 1; n <= nTimes; n++) { // Loop nTimes times
      const newFile = path.join(process.cwd(), `${startInd + n}${ext}`); // Set the new filename
      fs.copyFileSync(path.join(process.cwd(), file), newFile); // Copy the file with the new filename
      newFilesList.push(newFile); // Add the new file path to the newFilesList array
    }
  }

  function newTokenID(fileIncrement, newFilesList) {
    for (const i of newFilesList) { // Loop through each new file in the newFilesList array
      const name = path.basename(i); // Get the basename of the file
      const [nameNoExt, ext] = name.split('.'); // Split the filename into the name and extension parts
      const newTokenNum = parseInt(nameNoExt, 10).toString().padStart(6, '0'); // Parse the filename as an integer, convert it to a string, and pad it with leading zeros to 6 digits
      const newToken = `    "TokenID": ${newTokenNum},\n`; // Create the new "TokenID" line with the new token number
      const data = fs.readFileSync(i, 'utf-8').split('\n'); // Read the file and split the content into lines
      data[2] = newToken; // Replace the 3rd line with the new "TokenID" line
      fs.writeFileSync(i, data.join('\n'), 'utf-8'); // Write the modified content back to the file
    }
  }

  newTokenID(fileIncrement, newFilesList); // Call the newTokenID function with the fileIncrement function and the newFilesList array
}

fileIncrement(dirPath, nTimes); // Call the fileIncrement function with the specified directory path and number of times to copy each file
