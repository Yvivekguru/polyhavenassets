import bpy
from ..utils.is_ph_asset import is_ph_asset
from ..icons import get_icons
from ..ui import statusbar


class PHA_PT_asset_model(bpy.types.Panel):
    bl_label = " "
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "data"
    bl_parent_id = "OBJECT_PT_context_object"
    bl_options = {"HEADER_LAYOUT_EXPAND", "DEFAULT_CLOSED"}

    asset_id = ""

    @classmethod
    def poll(self, context):
        self.asset_id = is_ph_asset(context, context.object.instance_collection)
        return bool(self.asset_id)

    def draw_header(self, context):
        icons = get_icons()
        row = self.layout.row()
        row.label(text=f"Asset: {self.asset_id}", icon_value=icons["polyhaven"].icon_id)
        sub = row.row(align=True)
        sub.alignment = "RIGHT"
        if context.window_manager.pha_props.progress_total != 0:
            statusbar.ui(self, context, statusbar=False)
        else:
            sub.menu(
                "PHA_MT_resolution_switch_model",
                text=(context.object["res"] if "res" in context.object else "1k").upper(),
            )
        row.separator()  # Space at end

    def draw(self, context):
        layout = self.layout

        col = layout.column()
        col.label(text="Test!")
