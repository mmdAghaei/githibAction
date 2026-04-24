import { fetchExtensionZip } from 'chrome-extension-fetch';

(async () => {
    try {
        const { crxPath, zipPath } = await fetchExtensionZip(
            'https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc',
            {
                chromeVersion: '114.0.5735.133', // Optional: defaults to this version if not provided.
                outputDir: 'extensions' // Optional: defaults to "extensions"
            }
        );
        console.log('CRX saved at:', crxPath);
        console.log('ZIP saved at:', zipPath);
    } catch (error) {
        console.error('Failed to fetch extension:', error.message);
    }
})();