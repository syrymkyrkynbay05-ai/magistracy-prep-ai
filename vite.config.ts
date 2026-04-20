import path from 'path';
import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';
import { VitePWA } from 'vite-plugin-pwa';

export default defineConfig(({ mode }) => {
    const env = loadEnv(mode, '.', '');
    return {
      server: {
        port: 3000,
        host: '0.0.0.0',
      },
      plugins: [
        react(),
        VitePWA({
          registerType: 'autoUpdate',
          includeAssets: ['favicon.ico', 'apple-touch-icon.png', 'masked-icon.svg'],
          manifest: {
            name: 'MagisCore',
            short_name: 'MagisCore',
            description: 'Магистратураға дайындық',
            theme_color: '#348FE2',
            background_color: '#ffffff',
            display: 'standalone',
            icons: [
              {
                src: 'logo bg white, blue.png',
                sizes: '192x192',
                type: 'image/png'
              },
              {
                src: 'logo bg white, blue.png',
                sizes: '512x512',
                type: 'image/png'
              },
              {
                src: 'logo bg white, blue.png',
                sizes: '512x512',
                type: 'image/png',
                purpose: 'any maskable'
              }
            ]
          }
        })
      ],
      build: {
        target: 'esnext'
      },
      define: {
        'process.env.API_KEY': JSON.stringify(env.GEMINI_API_KEY),
        'process.env.GEMINI_API_KEY': JSON.stringify(env.GEMINI_API_KEY)
      },
      resolve: {
        alias: {
          '@': path.resolve(__dirname, '.'),
        }
      }
    };
});
