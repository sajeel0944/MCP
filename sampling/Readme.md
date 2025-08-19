CLIENT: "Hey server! Mujhe 'create_story' tool chahiye, topic hai: 'a function's adventure'"
SERVER: "Thik hai, ek second... (client se poochhta hai)"

SERVER --> CLIENT: "Zara story likh do is topic pe"

CLIENT: "Yeh lo! Teen sentence ki story ready hai!"

CLIENT --> SERVER: "Lo story wapas le lo"

SERVER: "Thanks! Ye lo CLIENT, tumhari mangi hui story!"

CLIENT: "Wah! Mil gayi! Terminal pe print karta hoon 😎"


(Client)                                 (Server)
   │                                         │
   │ call_tool("create_story", topic) ─────▶ │
   │                                         │
   │                          await ctx.session.create_message(...)
   │                                         │
   │ ◀────── sampling/create ─────────────── │
   │         (mock_sampler runs)            │
   │ ────── mock story returned ───────────▶ │
   │                                         │
   │     ◀────── story response ──────────── │
   │                                         │
print(story)                                 │
