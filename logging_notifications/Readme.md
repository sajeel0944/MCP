📰 [INFO] Configuration loaded successfully.
⚠️ [WARNING] Item failed validation.
❌ [ERROR] Failed to process item.
✅ Result: Failed to process item.



[CLIENT]                            [SERVER]

↓ Connect to MCP -----------------> Server starts

↓ Initialize session -------------> Server sends capabilities

↓ Call tool "process_item" ------> Server runs tool

← Receives log: "debug" <--------- ctx.debug(...)
← Receives log: "info"  <--------- ctx.info(...)
← Receives log: "warn"  <--------- ctx.warning(...)
← Receives log: "error" <--------- ctx.error(...)

← Receives result: "Failed..." <-- return TextContent(...)

Session ends
