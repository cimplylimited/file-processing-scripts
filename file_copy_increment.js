const fs = require('fs');
const path = require('path');

const dirPath = '/Users/johndoe/Git/LexDAO/LexDAO_Membership_Token';
const nTimes = 3;

function doCopy(dirPath, nTimes) {
  if (!fs.existsSync(dirPath)) {
    throw new Error('Directory does not exist.');
  }
  process.chdir(path.join(process.cwd(), dirPath));
  fs.readdirSync('.').forEach((file) => {
    if (!fs.statSync(file).isFile() || file[0] === '.') {
      return;
    }
    const { name, ext } = path.parse(file);
    console.log(`This is the original file name: ${name}`);
    const startInd = parseInt(name, 10);
    for (let n = 1; n <= nTimes; n++) {
      const newFile = path.join(process.cwd(), `${startInd + n}${ext}`);
      fs.copyFileSync(file, newFile);
    }
  });
}

doCopy(dirPath, nTimes);