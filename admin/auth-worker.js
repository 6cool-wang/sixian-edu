// Decap CMS OAuth proxy · 部署到 Cloudflare Workers
// 在 Cloudflare Dashboard → Workers & Pages → 创建 Worker → 粘贴此代码
// 设置环境变量: GH_CLIENT_ID, GH_CLIENT_SECRET, SITE_URL

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname === '/oauth/authorize') {
      const redirectUri = `${url.origin}/oauth/callback`;
      const state = url.searchParams.get('state');
      const ghUrl = `https://github.com/login/oauth/authorize?client_id=${env.GH_CLIENT_ID}&redirect_uri=${redirectUri}&scope=repo&state=${state}`;
      return Response.redirect(ghUrl);
    }

    if (url.pathname === '/oauth/callback') {
      const code = url.searchParams.get('code');
      const resp = await fetch('https://github.com/login/oauth/access_token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({
          client_id: env.GH_CLIENT_ID,
          client_secret: env.GH_CLIENT_SECRET,
          code,
        }),
      });
      const data = await resp.json();
      return Response.redirect(`${env.SITE_URL}/admin/#access_token=${data.access_token}`);
    }

    return new Response('Not found', { status: 404 });
  },
};
