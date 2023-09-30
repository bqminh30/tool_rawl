const fs = require('fs');

const filePath = './except1.txt';

function openFile() {
  try {
    const fileContents = fs.readFileSync(filePath, 'utf8');
    console.log(`Nội dung tệp: ${fileContents}`);
  } catch (error) {
    console.error(`Lỗi: ${error.message}`);
  }
}

openFile();
setInterval(() => {
  openFile();
}, 3600000); 
