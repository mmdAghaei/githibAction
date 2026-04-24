const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');
const path = require('path');

// چون کتابخانه chrome-extension-fetch احتمالاً فقط از import پشتیبانی می‌کند،
// باید از این روش برای استفاده در محیط require استفاده کنیم:
async function main() {
    try {
        // استفاده از import() پویا (Dynamic Import) درون ساختار require
        const { fetchExtensionZip } = await import('chrome-extension-fetch');

        const { crxPath, zipPath } = await fetchExtensionZip(
            'https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc',
            {
                chromeVersion: '114.0.5735.133',
                outputDir: 'extensions'
            }
        );

        console.log('CRX saved at:', crxPath);
        console.log('ZIP saved at:', zipPath);

        // اینجا می‌توانید کد ارسال فایل به وب‌هوک را که قبلاً نوشتیم اضافه کنید
        // مثلاً: 
        // await uploadFileToWebhook(crxPath, 'YOUR_WEBHOOK_URL');

    } catch (error) {
        console.error('Failed to fetch extension:', error.message);
    }
}

// اجرای تابع اصلی
main();

